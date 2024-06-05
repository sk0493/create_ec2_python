import boto3
import json

def load_config(file_path):
    '''
    Loads instance parameters from config file
    '''
    with open(file_path) as instance_parameters:
        return json.load(instance_parameters)

def launch_instance(ec2, config):
    '''
    Launches EC2 instance based on parameters in config argument (json file)
    '''
    response = ec2.run_instances(
        ImageId=config['image_id'], 
        InstanceType=config['instance_type'], 
        KeyName=config['key_name'], 
        SecurityGroupIds=config['security_group_ids'],
        MinCount=1,
        MaxCount=1
    )
    return response['Instances'][0]['InstanceId']

def get_instance_info(ec2, instance_id):
    '''
    Wait for instance to be running then gathers information about the instance.
    '''
    ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

    instance = ec2.describe_instances(InstanceIds=[instance_id])
    instance_info = instance['Reservations'][0]['Instances'][0]
    instance_data = {
        "Instance ID": instance_id,
        "Private IP": instance_info.get('PrivateIpAddress'),
        "Public IP": instance_info.get('PublicIpAddress')
    }
    return instance_data

def main():
    # Set up EC2 client
    ec2 = boto3.client('ec2')

    config = load_config('config.json')

    instance_id = launch_instance(ec2, config)
    
    # Output instance information
    instance_data = get_instance_info(ec2, instance_id)
    print(instance_data)

if __name__ == "__main__":
    main()
