# https://jaceklaskowski.github.io/spark-workshop/exercises/sql/Finding-Most-Populated-Cities-Per-Country.html


from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('batch_5').master('local[*]').getOrCreate()

df = spark.read.csv('batch_7.csv', header=True)
df.printSchema()
df.show(30, False)

df2 = df.select('name', 'country', 'population', f.regexp_replace(df['population'], r'\s+', '').cast('long').alias('population_long'))

country_window = Window.partitionBy('country').orderBy(f.desc('population_long'))

df3 = df2.withColumn('rownum', f.row_number().over(country_window))

df3.show(30, False)

df4 = df3.filter(df3['rownum'] == 1).drop('population_long', 'rownum')
df4.show(20, False)
spark.stop()
