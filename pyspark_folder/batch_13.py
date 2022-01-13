from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window

# https://jaceklaskowski.github.io/spark-workshop/exercises/sql/Calculating-Gap-Between-Current-And-Highest-Salaries-Per-Department.html

spark = SparkSession.builder.master('local[*]').appName('batch_13').getOrCreate()

df = spark.read.csv('batch_13.csv', header=True, inferSchema=True)
df.printSchema()

window = Window.partitionBy('department')

df2 = df.withColumn('max_in_department', f.max('salary').over(window))

df3 = df2.withColumn('diff', f.col('max_in_department') - f.col('salary'))
df3.show(20, False)

spark.stop()
