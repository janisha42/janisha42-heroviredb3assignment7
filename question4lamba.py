#Checking Unencrypted buckets

import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name='us-east-1')

    # Listing all the buckets 
    all_buckets = s3_client.list_buckets()['Buckets']

    # Check encryption status for each bucket
    for bucket in all_buckets:
        bucket_name = bucket['Name']
        encryption_status = _check_encryption_status(bucket_name, s3_client)

        if not encryption_status:
            print(f"Unencrypted Buckets: {bucket_name}")

def _check_encryption_status(bucket_name, s3_client):
    response = s3_client.get_bucket_encryption(Bucket=bucket_name)
    return response is not None
