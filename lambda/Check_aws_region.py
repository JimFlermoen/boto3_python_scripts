import json
import time
import os

def lambda_handler(event, context):
    databaseName = os.environ['AWS_REGION']
    print(databaseName)
   