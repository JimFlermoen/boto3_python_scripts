# Imports JSON and Boto3 libraries
import json
import boto3

# Imports the date and Time library
from datetime import datetime

#
def lambda_handler(event, context):
    
    now = datetime.now()    # Get the current datetime
    current_time = now.strftime('%H:%M:%S:%p')  # Displays the current datetime
                                                # as Hour:Min:Sec: am or pm
    sqs = boto3.client("sqs")  # Creates the SQS client
    
    
    
    
    sqs.send_message(      # Sends an SQS message to My Queue URL
        QueueUrl = 'arn:aws:sqs:us-east-1:277399983651:wk15_sqs_queue',
        
        MessageBody = current_time    # The message is the current time
        )
        
    return {
            'statusCode': 200, # Returns a status code of 200
            'body': json.dumps(current_time)  # Returns the current time
    }