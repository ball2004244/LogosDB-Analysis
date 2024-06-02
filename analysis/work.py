from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

url = r"hdfs://namenode:9870"
filepath = r"/twitter_data/tweets_v8.csv"

fullpath = url + filepath

sc = spark.sparkContext
df = spark.read.csv(fullpath)
df.show()