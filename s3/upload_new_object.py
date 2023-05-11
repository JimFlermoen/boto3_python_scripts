import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="jfler-boto-05092023", 
                Key="folder/foldera/folder1/test_text_string.txt", 
                Body="This is a string", 
                ContentType="text/plain")