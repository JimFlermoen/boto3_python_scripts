import boto3

# Get the service resource.
dynamodb = boto3.client('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Team_name',
            'AttributeType': 'S',  # 'S'means string
        },
        {
            'AttributeName': 'Location',
            'AttributeType': 'S',  # 'S' means string
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Team_name',
            'KeyType': 'HASH',  #  the Partition key
        },
        {
            'AttributeName': 'Location',
            'KeyType': 'RANGE',  # the Sort key
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,# The maximum number of strongly consistent reads 
        'WriteCapacityUnits': 5,# and writes consumed per second
    },
    # my table name
    TableName='NHL_Teams', 
)

# Print table status
print("Table status:", table.table_status) 