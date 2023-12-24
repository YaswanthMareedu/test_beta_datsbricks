# Databricks notebook source
from pyspark.sql import SparkSession
 
# Building the SparkSession and name
# it :'pandas to spark'
spark = SparkSession.builder.appName(
  "Git Test").getOrCreate()

# COMMAND ----------

input_path_test = '/mnt/bronze/dbo/testdt'
input_path_train = '/mnt/silver/dbo/traindt'

# COMMAND ----------

data = spark.read.format('csv').option("header", "true").load(input_path_train)
