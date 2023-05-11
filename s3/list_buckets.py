import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all buckets in S3
response = s3.list_buckets()

# Extract the list of buckets
buckets = response['Buckets']

# Iterate over each bucket and print its name and creation date
for bucket in buckets:
    print(bucket["Name"], bucket["CreationDate"])