from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

# Load data from HDFS
df = spark.read.option("header", "true").csv("hdfs://namenode:9000/data/raw/your_table")

# Data Cleaning & Transformation
df = df.withColumn("formatted_date", to_date(col("date_column"), "yyyy-MM-dd"))

# Write processed data to S3
df.write.mode("overwrite").parquet("s3://your-s3-bucket/processed/your_table")

print("Data processing complete!")
