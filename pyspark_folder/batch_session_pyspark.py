from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *

data_schema = StructType(
    [
        StructField('name', StringType()),
        StructField('event_time', StringType())
    ]
)


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.read.csv(path='data.csv', sep=',', header=True, schema=data_schema)
df = df.select('name', f.translate("event_time", ' ', '').cast('long').alias('event_time_long')).\
    drop('event_time').\
    withColumnRenamed('event_time_long', 'event_time')
df.show(20, False)

max_session_limit = 600 # 10 mins
window_1 = Window.partitionBy('name').orderBy('event_time')

df.printSchema()


df2 = df.withColumn("prev_event_time", f.lag(df["event_time"], 1).over(window_1))
df2 = df2.select('name', 'event_time', 'prev_event_time',
                 (df2["event_time"].cast('long') - df2["prev_event_time"].cast('long')).alias('difference'),
                 f.when((df2["event_time"].cast('int') - df2["prev_event_time"].cast('int')) < max_session_limit, 0).otherwise(1).alias('isSession'))
df2.show(20, False)

df2 = df2.select('name', 'event_time', f.sum('isSession').over(window_1).alias('sessionid'))
df2.show(20, False)

df3 = df2.groupBy('name', 'sessionid').agg(f.min('event_time').alias('min_event_time'), f.max('event_time').alias('max_event_time'), f.count("*").alias('count'))

df3.show(20, False)

spark.stop()
