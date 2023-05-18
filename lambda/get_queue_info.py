import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/277399983651/wk15_sqs_queue'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])