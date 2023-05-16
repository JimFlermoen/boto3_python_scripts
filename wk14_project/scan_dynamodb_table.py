import boto3

# Create the client for DynamoDB
dynamodb = boto3.client("dynamodb")

# scan my DynamoDB table, named NHL_Teams
response = dynamodb.scan(TableName='NHL_Teams')

# Iterate over the scanned items
for item in response['Items']:
    # Print the team name and location
    print(item['Team_name'], (item['Location']))