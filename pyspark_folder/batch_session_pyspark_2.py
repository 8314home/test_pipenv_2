from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *

# considering a session will be inactive after 600 sec of without activity,
# so difference between current_click_time and prev_click_time < 600
# ie (current_click_time - prev_click_time) < 600

# Additional, start of session , the session can remain active upto  1000 sec
# ie if session start is at 1 timestamp, then at 1001 it will auto expire

# Use of Window:  Window.partitionBy('name').orderBy(f.asc('event_time'))
# Use of translate() function to replace any unwanted characters
# groupBy().agg(f.max,f.min,f.count("*"))

data_schema = StructType(
    [
        StructField('name', StringType()),
        StructField('event_time', StringType())
    ]
)


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.read.csv(path='data.csv', sep=',', header=True, schema=data_schema)
df = df.select('name', f.translate("event_time", ' ', '').cast('long').alias('event_time_long')). \
    drop('event_time'). \
    withColumnRenamed('event_time_long', 'event_time')
df.show(20, False)

max_inactivity_limit = 300 # 5 mins
max_session_duration = 1000 # 1000 seconds
window_1 = Window.partitionBy('name').orderBy(f.asc('event_time'))

df.printSchema()


df2 = df.withColumn("prev_event_time", f.lag(df["event_time"], 1).over(window_1)).\
    withColumn('start_of_session', f.first(df["event_time"]).over(window_1))

df2 = df2.select('name', 'event_time', 'prev_event_time',
                 (df2["event_time"].cast('long') - df2["prev_event_time"].cast('long')).alias('difference'),
                 f.when(((df2["event_time"].cast('int') - df2["prev_event_time"].cast('int')) <= max_inactivity_limit) & (df2["event_time"] < df2["start_of_session"].cast('int') + max_session_duration)
                        , 0).otherwise(1).alias('isSession'))
df2.show(20, False)

df2 = df2.select('name', 'event_time', f.sum('isSession').over(window_1).alias('sessionid'))
df2.show(20, False)

df3 = df2.groupBy('name', 'sessionid').agg(f.min('event_time').alias('min_event_time'), f.max('event_time').alias('max_event_time'), f.count("*").alias('count'))

df4 = df3.withColumn('user_sessionid', f.concat(f.col('name'), f.lit('_'), f.col('sessionid')))

df4.show(20, False)

spark.stop()