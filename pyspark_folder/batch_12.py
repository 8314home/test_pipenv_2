from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import window
from pyspark.sql import udf

# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Difference-in-Days-Between-Dates-As-Strings.html

spark = SparkSession.builder.master("local[*]").appName('batch_12').getOrCreate()

input_data = [
    ("08/11/2015",),
    ("09/11/2015",),
    ("09/12/2015",)
        ]
#df = spark.read.csv('batch_7.csv', header=True)

df = spark.createDataFrame(input_data, ["date_string"])

df.printSchema()

df = df.withColumn('date_formated', f.to_date('date_string', "dd/MM/yyyy")).withColumn('current_date', f.current_date()).withColumn('date_diff', f.datediff(f.col('current_date'), f.col('date_formated')))

df.show(20, False)


spark.stop()
