import boto3

subnet_id = "subnet-03cea7d5a0e2fc756"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)
