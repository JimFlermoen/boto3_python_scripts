import boto3

route_table_id = "rtb-0cb7fc70dedd2aecf"
internet_gateway_id = "igw-0266242255baaa8f2"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GateWayId=internet_gateway_id,
    RouteTableId=route_table_id
)