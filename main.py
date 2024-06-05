import boto3
import json

# Set EC2 client
ec2 = boto3.client('ec2')

# Load instance parameters from config file
with open('config.json') as instance_parameters:
    config = json.load(instance_parameters)

# Instance parameters
image_id = config['image_id']
instance_type = config['instance_type']
key_name = config['key_name']
security_group_ids = config['security_group_ids']

# Launch EC2 instance
response = ec2.run_instances(
    ImageId=image_id, 
    InstanceType=instance_type, 
    KeyName=key_name, 
    SecurityGroupIds = security_group_ids,
    MinCount=1,
    MaxCount=1
    )

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']

# Wait for instance to be running then execute next code
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Prints instance information
instance = ec2.describe_instances(InstanceIds=[instance_id])
instance_info = instance['Reservations'][0]['Instances'][0]

print(f"Instance ID: {instance_id}")
print(f"Private IP: {instance_info.get('PrivateIpAddress')}")
print(f"Public IP: {instance_info.get('PublicIpAddress')}")

