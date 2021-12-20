# https://jaceklaskowski.github.io/spark-workshop/exercises/sql/Finding-Ids-of-Rows-with-Word-in-Array-Column.html

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