import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Read processed data from S3
df = spark.read.parquet("s3://your-s3-bucket/processed/your_table")

# Snowflake connection options
sf_options = {
    "sfURL": "https://your-snowflake-account.snowflakecomputing.com",
    "sfDatabase": "YOUR_DB",
    "sfSchema": "PUBLIC",
    "sfWarehouse": "COMPUTE_WH",
    "sfRole": "SYSADMIN",
    "user": "your_user",
    "password": "your_password"
}

# Write to Snowflake
df.write \
    .format("snowflake") \
    .options(**sf_options) \
    .option("dbtable", "processed_data") \
    .mode("overwrite") \
    .save()

print("Data successfully loaded into Snowflake!")
