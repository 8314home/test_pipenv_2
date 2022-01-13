from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window
from pyspark.sql.types import *
from pyspark.sql.functions import udf

# https://jaceklaskowski.github.io/spark-workshop/exercises/sql/Multiple-Aggregations.html
# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Collect-values-per-group.html
# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Using-UDFs.html

spark = SparkSession.builder.master('local[*]').appName('batch_14').getOrCreate()

df = spark.range(10).withColumn('group', f.col('id') % 2)
df.show()

df2 = df.groupBy('group').agg(f.min(f.col('id')).alias('min_value'), f.max(f.col('id')).alias('max_value'))
df2.show()


df3 = df.groupBy('group').agg(f.collect_list('id').alias('id_list'))
df3.show()

# UDF usage via spark SQL


def my_fn(s: str):
    return str.upper(s)


spark.udf.register("custom_upper_value", my_fn, StringType()) ## session level registration

df4 = spark.read.csv('batch_7.csv',header=True, inferSchema=True)
df4.createOrReplaceTempView('my_table')
df5 = spark.sql('select *, custom_upper_value(country) from my_table')

df5.show()

# UDF usage via dataframe

custom_upper_value = udf(lambda l: my_fn(l))  ## call from pyspark library, not that lambda fn is needed to iterate through each row
df6 = df4.select(custom_upper_value(f.col('country')).alias('df_udf_country_upper'))
df6.show(20)


spark.stop()
