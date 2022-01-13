from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window
from pyspark.sql.types import *

# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Why-are-all-fields-null-when-querying-with-schema.html

spark = SparkSession.builder.master('local[*]').appName('batch_14').getOrCreate()


input_schema = StructType(
    [
        StructField('time_value', TimestampType()),
        StructField('ip', StringType()),
        StructField('extra', StringType())
    ]
)

df = spark.read.option("timestampFormat", "yyyy-MM-dd HH:mm:ss,SSS").csv('batch_14.csv', schema=input_schema, sep='|')


df.drop('extra').show(20, False)


spark.stop()