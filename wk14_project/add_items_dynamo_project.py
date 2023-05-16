import boto3  # Import the Boto3 library

# Create a client for DynamoDB
dynamodb = boto3.client('dynamodb')

# Put a single item into my DynamoDB table
response = dynamodb.put_item(
    Item={
        'Team_name': {
            'S': 'Boston Bruins',
        },
        'Location': {
            'S': 'TD Garden Arena, Boston, MA',
        },
        'Rank': {
            'N': '1',
        },
    },
    ReturnConsumedCapacity='TOTAL',  # The consumed capacity information to be returned
    TableName='NHL_Teams',  # My table name of the DynamoDB table
)