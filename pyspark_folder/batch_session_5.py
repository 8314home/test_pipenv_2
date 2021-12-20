from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window

# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Using-Dataset-flatMap-Operator.html
# https://stackoverflow.com/questions/64041530/create-dataframe-with-arraytype-column-in-pyspark


spark = SparkSession.builder.appName('batch_5').master('local[*]').getOrCreate()

input_data = [
    ([1,2,3],)    # notice it is a tuple with 1 element so mention like this (x,)
]

df = spark.createDataFrame(input_data, ['nums'])
df.printSchema()
df.show(10, False)

df2 = df.select(df['nums'], f.explode(df['nums']).alias('num'))
df2.show(30, False)

spark.stop()
