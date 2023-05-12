import boto3

def get_vpc_information(client, Filters=[]):
    response = ec2.describe_vpcs(Filters=Filters)
    for vpc in response["Vpcs"]:
        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])

def get_vpc_name(client, Filters=[]):
    response = ec2.describe_vpcs(Filters=Filters)
    for vpc in response["Vpcs"]:
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if "Name" == tag['Key']:
                        print(tag["Value"])

if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    
    Filters=[{'Name': 'isDefault','Values': ['true',]},]
        
    get_vpc_information(ec2)
    get_vpc_information(ec2, Filters)