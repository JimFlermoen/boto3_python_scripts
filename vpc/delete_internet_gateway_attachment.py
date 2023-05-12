import boto3

internet_gateway_id = "igw-0266242255baaa8f2"
vpc_id = "vpc-097089307088f4a72"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)