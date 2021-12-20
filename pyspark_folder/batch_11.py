from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window
from pyspark.sql import udf
from pyspark.storagelevel import StorageLevel


# https://stackoverflow.com/questions/37077432/how-to-estimate-dataframe-real-size-in-pyspark



spark = SparkSession.builder.appName('batch_11').master('local[4]').getOrCreate()

print(spark.sparkContext.getConf().getAll())

df = spark.read.csv('sales.csv')
df_sampled = df.sample(0.01)

print(spark.sparkContext.applicationId)

df_sampled.persist(StorageLevel.MEMORY_ONLY)
print(df_sampled.count())
# get samples no of records count (base of sample fraction) multiply by size of it in memory & compute total size

df_sampled.unpersist()
spark.stop()
