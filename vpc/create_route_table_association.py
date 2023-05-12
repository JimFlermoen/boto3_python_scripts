import boto3

route_table_id = "rtb-0cb7fc70dedd2aecf"
subnet_id = "subnet-03cea7d5a0e2fc756"

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])