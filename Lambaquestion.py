# Automated Instance Management Using AWS Lambda and Boto3 - Auto Stop and Auto Start Tags

import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Auto Stopping Instances 
    
    auto_stop_instances = ec2_client.describe_instances(Filters=[{'Name': 'tag:Auto-Stop', 'Values': ['True']}])
    for reservation in auto_stop_instances['Reservations']:
        for instance in reservation['Instances']:
            ec2_client.stop_instances(InstanceIds=[instance['InstanceId']])
            print(f'Stopping instance: {instance["InstanceId"]}')

    # Auto Starting Instances
    
    auto_start_instances = ec2_client.describe_instances(Filters=[{'Name': 'tag:Auto-Start', 'Values': ['True']}])
    for reservation in auto_start_instances['Reservations']:
        for instance in reservation['Instances']:
            ec2_client.start_instances(InstanceIds=[instance['InstanceId']])
            print(f'Starting instance: {instance["InstanceId"]}')
