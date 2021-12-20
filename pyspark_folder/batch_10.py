from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import udf
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('json_read').master('local[4]').getOrCreate()

df = spark.read.json('batch_10_json_file.json', multiLine=True)
df.printSchema()
df.show(20, False)

# array to multiple rows -explode()
df = df.select('key', f.explode('columns').alias('column'))
df.printSchema()
df.show(20, False)

# break array to different columns (list with different elemnet types)  -index based access
df = df.select('key', f.col('column')[0].alias('event'), f.col('column')[1].alias('data'), f.col('column')[2].alias('epoch_time'))
df.printSchema()
df.show(20, False)

# string to array within same column
# take individual element from array to create new column
# take a slice to keep a slice of array in column
# f.split(f.translate('event', '\\', ''), ':').alias('event_parts')
# f.slice(f.split(f.translate('event', '\\', ''), ':'), 2, 3).alias('event_parts')

df = df.select('key',
               f.split(f.translate('event', '\\', ''), ':')[0].alias('event_str'),
               f.split(f.translate('event', '\\', ''), ':')[4].alias('json_flag'),
               f.slice(f.split(f.translate('event', '\\', ''), ':'), 2, 3).alias('event_parts'),
               'epoch_time',
               f.get_json_object(f.col('data'), '$.user.credType').alias('user_credtype'),
               f.get_json_object(f.col('data'), '$.user.credValue').alias('user_credvalue'),
               f.get_json_object(f.col('data'), '$.user.cAgent').alias('user_cagent'),
               f.get_json_object(f.col('data'), '$.user.cType').alias('user_ctype'),
               f.get_json_object(f.col('data'), '$.timestamp').alias('timestamp'),
               f.get_json_object(f.col('data'), '$.sessionId').alias('sessionId'),
               f.get_json_object(f.col('data'), '$.className').alias('className'),
               f.get_json_object(f.col('data'), '$.subtype').alias('subtype'),
               f.get_json_object(f.col('data'), '$.vType').alias('vType'),
               f.get_json_object(f.col('data'), '$.vId').alias('vId'),
               f.get_json_object(f.col('data'), '$.eType').alias('eType'),
               f.get_json_object(f.col('data'), '$.eData').alias('eData'),
               f.get_json_object(f.col('data'), '$.user').alias('user'),
               )
df.printSchema()
df.show(20, False)

# split to create array with elements from a string column
# f.split(f.translate('event', '\\', ''), ':')
# array_join function to join array elements within a column into string
# f.array_join('event_parts', ':')

# simple dateformat - formats https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

df = df.drop('user').withColumn('event_timestamp', f.array_join('event_parts', ':')).drop('event_parts')
df = df.withColumn('event_timestamp_utc', f.to_timestamp(f.col('event_timestamp'), "yyyy-MM-dd HH:mm:ssX"))
df.printSchema()
df.show(20, False)



spark.stop()
