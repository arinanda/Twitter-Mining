from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext
import sys
import requests

conf = SparkConf()
conf.setAppName("TwitterStreamApp")