# Delete Objects older than 30 days from s3

import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_name = 'janishab3'
    
    objects = s3_client.list_objects_v2(Bucket=bucket_name)['Contents']

    current_date = datetime.now()

    # Delete objects older than 30 days 
    for obj in objects:
        last_modified = obj['LastModified'].replace(tzinfo=None)
        if (current_date - last_modified) > timedelta(days=30):
            
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Deleted: {obj['Key']}")

    return {
        'statusCode': 200,
        'body': 'S3 Bucket Cleanup Complete!'
    }
