from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import udf
from pyspark.sql.window import Window

# https://adatis.co.uk/parsing-nested-json-lists-in-databricks-using-python/

spark = SparkSession.builder.appName('json_read').master('local[4]').getOrCreate()

df = spark.read.json('sample2.json', multiLine=True)
df.printSchema()
df.show(20, False)

df2 = df.select(f.explode('persons').alias('persons'))
df2.printSchema()
df2.show(20, False)

df3 = df2.select(f.col('persons.name').alias('person_name'), f.col('persons.age').alias('person_age'), f.col('persons.cars').alias('person_cars'))
df3.printSchema()
df3.show(20, False)

df4 = df3.select('person_name', 'person_age', f.explode('person_cars').alias('person_car'))
df4.printSchema()
df4.show(20, False)

df5 = df4.select('person_name', 'person_age', f.explode('person_car.models').alias('person_car_model'), f.col('person_car.name').alias('person_car_model_make'))
df5.printSchema()
df5.show(20, False)

spark.stop()
