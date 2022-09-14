# import boto3
# from botocore.exceptions import ClientError
from models.secret_model import Secret

# client = boto3.client('secretsmanager')



def create_secret(secret: Secret):
    response = client.create_secret(
        Name = secret.name        
    )
