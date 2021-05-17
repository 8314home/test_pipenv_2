from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import os
import sys
from configparser import ConfigParser
from pyspark.sql.types import *

staging_glb_marketing_cost_schema = StructType(
    [
        StructField("report_date", StringType(), True),
        StructField("country_id", StringType(), True),
        StructField("ref_attr_class_key", StringType(), True),
        StructField("demand_channel", StringType(), True),
        StructField("cost_local", StringType(), True),
        StructField("currency_code", StringType(), True),
        StructField("department_id", StringType(), True),
        StructField("user_brand_affiliation", StringType(), True),
        StructField("modified_at_date", StringType(), True),
        StructField("uploaded_to_cube", StringType(), True),
    ]
)


app_name = 'global_display_hive_to_td_global_marketing_cost'
master = 'yarn'
source_file = 'hdfs://cerebro-namenode/user/grp_gdoop_ima/ima_hiveDB.db/glb_marketing_cost/'
target_table = 'sandbox.staging_glb_marketing_cost'
user = "gp_etl_ops"
password = 'C4d91b3b15'
url = "jdbc:teradata://tdwd/DATABASE=sandbox"


# Create Spark session
spark = SparkSession.builder \
    .appName(app_name) \
    .master(master) \
    .config("spark.yarn.queue", "dse_reserved") \
    .getOrCreate()
driver = 'com.teradata.jdbc.TeraDriver'

df = spark.read.csv(source_file, sep='\t')

df.write.jdbc(url=url, mode='overwrite',table=target_table, properties={'user': user, 'password': password, 'driver': driver})

#
#
# def load_data(driver, jdbc_url, sql, user, password):
#     return spark.read \
#         .format('jdbc') \
#         .option('driver', driver) \
#         .option('url', jdbc_url) \
#         .option('dbtable', '({sql}) as src'.format(sql=sql)) \
#         .option('user', user) \
#         .option('password', password) \
#         .load()
#


print("data write completed.stopping spark session.")
spark.stop()
