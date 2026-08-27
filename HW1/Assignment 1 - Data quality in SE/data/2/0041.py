

from pyspark import SparkContext, SparkConf
import time 

# Create a basic configuration
conf = SparkConf().setAppName("myTestCopyApp")

# Create a SparkContext using the configuration
sc = SparkContext(conf=conf)

print("START")

time.sleep(30)

print("END")
