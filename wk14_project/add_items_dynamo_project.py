import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'Team_name':{
          'S': 'Boston Bruins'  ,
        },
        'Location': {
            'S': 'TD Garden Arena, Boston, MA',
        },
        'Rank': {
            'N': '1',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='NHL_Teams',
)