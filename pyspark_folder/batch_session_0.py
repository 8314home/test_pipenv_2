


from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec

spark = SparkSession.builder.appName('testapp').master('local[*]').getOrCreate()


##https://jaceklaskowski.github.io/spark-workshop/exercises/sql/split-function-with-variable-delimiter-per-row.html
input_list = [
    ("50000.0#0#0#", "#"),
    ("0@1000.0@", "@"),
    ("1$", "$"),
    ("1000.00^Test_string", "^")
]

rdd = spark.sparkContext.parallelize(input_list)
df = rdd.toDF(['value', 'delim'])
df.show(20, False)

df = df.rdd.map(lambda l: (l[0], l[1], l[0].split(l[1]))).toDF(['value', 'delim', 'after_split'])
df.show(20, False)

#--------------------

##https://jaceklaskowski.github.io/spark-workshop/exercises/sql/selecting-the-most-important-rows-per-assigned-priority.html

input_list = [
    (1, "MV1"),
    (1, "MV2"),
    (2, "VPV"),
    (2, "Others")
]

rdd = spark.sparkContext.parallelize(input_list)
df = rdd.toDF(['priority', 'value'])
df.show(20, False)

df.groupBy(df['priority']).agg(f.first(df['value']).alias('most_important_row')).show(20, False)


#--------------------

#https://jaceklaskowski.github.io/spark-workshop/exercises/sql/adding-count-to-the-source-dataframe.html

input_list = [
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604900", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604899", "10.0.0.2.54880", "10.0.0.3.5001",  2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2),
    ("05:49:56.604908", "10.0.0.3.5001",  "10.0.0.2.54880", 2)
]

rdd = spark.sparkContext.parallelize(input_list)
df = rdd.toDF(["column0", "column1", "column2", "label"])
df.show(30, False)

window_col1_col2 = Window.partitionBy(df['column1'], df['column2']).orderBy(df['column1'], df['column2'])

df.withColumn('row_numbers', f.row_number().over(window_col1_col2)).withColumn('row_counts', f.max('row_numbers').over(window_col1_col2)).show(30, False)

spark.stop()

#---------------------------------

#https://jaceklaskowski.github.io/spark-workshop/exercises/sql/limiting-collect_set-standard-function.html

spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.range(50)
df = df.withColumn("key", df['id'] % 5)
df.show(20, False)

df = df.groupBy('key').agg(f.collect_set('id').alias('all_values'))
df = df.withColumn('first_three_value', f.slice(df['all_values'], 1, 3))
df.show(20, False)

spark.stop()

#---------------------------------

#https://jaceklaskowski.github.io/spark-workshop/exercises/sql/structs-for-column-names-and-values.html

# #https://jaceklaskowski.github.io/spark-workshop/exercises/sql/structs-for-column-names-and-values.html

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *

# define nested schema

ratings_schema = StructType([
    StructField('movie_name', StringType()),
    StructField('rating', StringType())
])

input_schema = StructType([
    StructField('name', StringType()),
    StructField('ratings', ArrayType(ratings_schema))
])

input_list = [
    ("Manuel", [("Logan", 1.5), ("Zoolander", 3), ("John Wick", 2.5)]),
    ("John", [("Logan", 2), ("Zoolander", 3.5), ("John Wick", 3)])
]


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

rdd = spark.sparkContext.parallelize(input_list)
df = spark.createDataFrame(rdd, input_schema)  # create dataframe from rdd and apply nested schema
df.show(10, False)
df.printSchema()

df = df.withColumn('exploded_ratings', f.explode(df['ratings'])).drop(df['ratings'])  # 1 to many rows
df.show(20, False)
df.printSchema()

df = df.select('name', 'exploded_ratings.*')  # converting array to multiple columns
df.show(20, False)
df.printSchema()

df = df.groupBy('name').pivot('movie_name').agg(f.max('rating'))  # pivot to convert column values to column
df.show(20, False)

spark.stop()

#--------------------


# #https://jaceklaskowski.github.io/spark-workshop/exercises/sql/merge-two-rows.html

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *

input_schema = StructType([
    StructField('id', StringType(), False),
    StructField('name', StringType(), False),
    StructField('age', StringType(), True),
    StructField('place', StringType(), True)
])

input_list = [
    ("100", "John", 35, None),
    ("100", "John", None, "Georgia"),
    ("101", "Mike", 25, None),
    ("101", "Mike", None, "New York"),
    ("103", "Mary", 22, None),
    ("103", "Mary", None, "Texas"),
    ("104", "Smith", 25, None),
    ("105", "Jake", None, "Florida")
]


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.createDataFrame(input_list, input_schema)
df.show(20, False)
df.printSchema()

df = df.groupBy('id', 'name').agg(f.max('age').alias('age'), f.max('place').alias('place'))
df.show(20, False)

spark.stop()


#------------------------
# #https://jaceklaskowski.github.io/spark-workshop/exercises/sql/explode-structs-array.html

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.read.json('explode_array.json', multiLine=True)
df.printSchema()
df.show(20, False)

# #https://medium.com/@koushikweblog/pivot-unpivot-data-with-sparksql-pyspark-databricks-89f575f3b3ed

list_of_days = df.select('hours.*').columns  # access columns and prepare string for stack function inside spark SQL
print(list_of_days)
len_lof_of_days = len(list_of_days)

final_list = [f"'{x}'"+"," + x for x in list_of_days]
print(final_list)
final_string = ",".join(final_list)
print(final_string)
print('select business_id,full_address,stack({0},{1}) as (day,hours) from sql_table'.format(len_lof_of_days, final_string))

# select business_id,full_address,stack(7,'Friday',Friday,'Monday',Monday,'Saturday',Saturday,'Sunday',Sunday,'Thursday',Thursday,'Tuesday',Tuesday,'Wednesday',Wednesday) as (day,hours) from sql_table

df = df.select('business_id', 'full_address', 'hours.*')
df.show(30, False)
tbl = df.registerTempTable('sql_table')  # register table

# this is unpivot operation is done using spark-SQL stack() function
df2 = spark.sql('select business_id,full_address,stack({0},{1}) as (day,hours) from sql_table'.format(len_lof_of_days, final_string))
df2.show(30, False)

df2.select("*", "hours.open", "hours.close").drop("hours").orderBy("business_id", "full_address", "day", "open", "close").show(30, False)


spark.stop()
#----------------------


#---------------------

# #https://jaceklaskowski.github.io/spark-workshop/exercises/sql/Finding-Ids-of-Rows-with-Word-in-Array-Column.html

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.window import Window, WindowSpec
from pyspark.sql.types import *


# Input Dataset
# +---+------------------+-----+
# | id|             words| word|
# +---+------------------+-----+
# |  1|     one,two,three|  one|
# |  2|     four,one,five|  six|
# |  3|seven,nine,one,two|eight|
# |  4|    two,three,five| five|
# |  5|      six,five,one|seven|
# +---+------------------+-----+
input_list = [
    (1, "one,two,three", 'one'),
    (2, "four,one,five", 'six'),
    (3, "seven,nine,one,two", 'eight'),
    (4, "two,three,five", 'five'),
    (5, "six,five,one", 'seven')
]


spark = SparkSession.builder.appName('batch_pyspark_session').master('local[4]').getOrCreate()

df = spark.createDataFrame(input_list, ['id', 'words', 'word'])
df.show()

df = df.select(df['id'], f.split(df['words'].cast('string'), ',').alias('words_array'))
df = df.select(df['id'], f.explode('words_array').alias('w'))

df.show(20, False)

df = df.groupBy('w').agg(f.collect_list('id').alias('ids'))

df = df.select(df['w'], f.concat_ws(',', df['ids']).alias('list_of_ids'))
df.printSchema()
df.show(20, False)

spark.stop()

# o/p
#
# root
# |-- w: string (nullable = true)
# |-- lis_of_ids: string (nullable = false)
#
# +-----+----------+
# |w    |lis_of_ids|
# +-----+----------+
# |two  |1,3,4     |
# |seven|3         |
# |four |2         |
# |one  |1,2,3,5   |
# |six  |5         |
# |nine |3         |
# |three|1,4       |
# |five |2,4,5     |
# +-----+----------+