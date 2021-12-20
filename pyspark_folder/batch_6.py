from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window

# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Flattening-Array-Columns-From-Datasets-of-Arrays-to-Datasets-of-Array-Elements.html

spark = SparkSession.builder.appName('batch_5').master('local[*]').getOrCreate()

input_data = [
    (["a", "b", "c"],),
    (["X", "Y", "Z"],)    # notice it is a tuple with 1 element so mention like this (x,)
]

df = spark.createDataFrame(input_data, ['data'])
df.printSchema()

df_columns = df.columns
df.show(20, False)

df2 = df.select(df['data'], f.posexplode(df['data']))
df2.show(30, False)

df2 = df2.groupBy('data').pivot('pos').agg(f.first('col'))
df2.show(30, False)

df3 = df2.drop('data')
df3.show(30, False)

spark.stop()
