import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object',Params={'Bucket': "jfler-boto-05092023",'Key': "test_text_.txt"},ExpiresIn=300)

print(response)