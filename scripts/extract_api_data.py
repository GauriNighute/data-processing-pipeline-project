import requests
import boto3
import json

API_URL = "https://api.example.com/data"
S3_BUCKET = "your-s3-bucket"
S3_KEY = "raw/api_data.json"

def extract_data():
    response = requests.get(API_URL)
    data = response.json()
    
    s3 = boto3.client('s3')
    s3.put_object(Body=json.dumps(data), Bucket=S3_BUCKET, Key=S3_KEY)

    print("Data successfully uploaded to S3.")

if __name__ == "__main__":
    extract_data()
