from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.functions import Column
from pyspark.sql.window import Window

# Apply functions from a list of dictionaries to spark columns

spark = SparkSession.builder.appName('batch_5').master('local[*]').getOrCreate()

df = spark.read.csv('batch_7.csv', header=True)
cols = df.schema.names

df.printSchema()

# df.select(f.upper(f.col('name')), f.lower(f.col('country')), f.translate(f.col('population'),' ', '')).show()

d = {
    'name': 'upper',
    'country': 'lower',
    'population': 'md5'
}
s = ""
for x in cols:
    if x in d:
        fn = d[x]
        s = f"{fn}({x}) as {x}_derived"
        print(s)
        df = df.selectExpr("*", f"{s}").drop(f"{x}")

df.printSchema()

df.show(20, False)

spark.stop()
