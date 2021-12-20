# https://jaceklaskowski.github.io/spark-workshop/exercises/spark-sql-exercise-Reverse-engineering-Dataset-show-Output.html

from pyspark.sql import SparkSession
from pyspark.sql import functions as f

# csv() options
# :param comment: sets a single character used for skipping lines beginning with this
# character. By default (None), it is disabled.
# :param header: uses the first line as names of columns. If None is set, it uses the
# default value, ``false``.

# df.columns to get columns names and remove 1st and last

spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.read.csv('dataset_show_output_read.csv', sep='|', comment='+', header=True)
df.printSchema()
columns = df.columns
df.drop(columns[0], columns[-1]).show(20, False)

print("--Using text()---")

df2 = spark.read.text('dataset_show_output_read.csv')
df2.printSchema()

# remove comments
df2 = df2.withColumn('flag', f.when(df2['value'].startswith('+'), '0').otherwise('1')).filter("flag = 1").drop("flag")

# take first row as header, derive column names by accessing row object
header_record = df2.first()
header_df = spark.sparkContext.parallelize([header_record]).toDF(['values'])
print(header_record)
df_columns = header_record[0].split('|')
print(df_columns)


# # RDD format filter out all records except the header, then split with |, finally convert to df and drop '' columns
# df3 = df2.rdd.filter(lambda l: l != header_record).map(lambda l: l[0].split('|')).toDF(df_columns).drop('')
# df3.show(30, False)

print("--Using Dataframe--")

# subtract header df from original df
df4 = df2.subtract(header_df)
df4 = df4.rdd.map(lambda l: l[0].split('|')).toDF(df_columns).drop('')
df4.show(20, False)

spark.stop()

