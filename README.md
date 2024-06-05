# Introduction

Python script that uses the boto3 library to launch a EC2 instance. A separate json config file contains the parameters of the ec2 instances to be created.

boto3 documentation:
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

## Why use Python to manage cloud resources

Although you can use Terraform or the AWS UI to create and manage EC2 instances, in some cases Python can be better. 

- You can automatically provision resources based on application or business requirements.
- Python scripts can leverage custom metrics that are not natively supported by AWS auto-scaling.
- Using Python you have more granular control and gives you the option to have highly customized solutions 
- Python can interact with many other APIs. 

For example if you have an trading/investment website, you can track the stock price or market alerts. If certain tresholds are met you can use Python conditional statements to run a function that create EC2 instances automatically so that your website is ready for the high traffic.

# Requirements

- boto3
- aws configure



