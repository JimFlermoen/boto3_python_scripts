import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
   InstanceId='i-03073618e81c158a8',
    Name='Go to Ami'
)

print(response["ImageId"])