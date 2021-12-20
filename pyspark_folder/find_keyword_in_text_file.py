from pyspark.sql import SparkSession
from pyspark.sql import functions as f

input_text = 'Hello'

spark = SparkSession.builder.master('local[4]').appName('text_file_reader').getOrCreate()

rdd1 = spark.read.text('sample-2mb-text-file.txt').rdd

print('No of partitions - {}'.format(rdd1.getNumPartitions()))

rdd2 = rdd1.flatMap(lambda line: line.value.split(" "))
rdd2 = rdd2.map(lambda word: 1 if word == input_text else 0)
print('No of partitions after map - {}'.format(rdd2.getNumPartitions()))

# collect to final variable- reduce is an action, reduces to 1 value

final_variable = rdd2.reduce(lambda x, y: x+y)

if final_variable:
    print(f'{final_variable} Text present')
else:
    print('Not present')

# 2nd method - faster
#rdd1 = spark.read.text('sample-2mb-text-file.txt').rdd
final_variable_2 = rdd2.map(lambda word: 1 if word == input_text else 0).filter(lambda x: x).getNumPartitions()
if final_variable_2:
    print(f'{final_variable_2} Text present')
else:
    print('Not present')

spark.stop()

