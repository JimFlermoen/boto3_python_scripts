import boto3

vpc_id = "vpc-097089307088f4a72"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
