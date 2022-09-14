import boto3
from botocore.exceptions import ClientError
import json
import datetime

# COMMON VARS
NOW = datetime.datetime.now()
CLIENT = boto3.client('secretsmanager')

#Handling JSON file
FILE = open('../vars.json')

#Creating a Dictonary with data
DIC = json.load(FILE)

#Interating throught the JSON list
for x in DIC['inputs']:
  print(NOW)
  print(DIC)


# client = boto3.client('secretsmanager')

# response = client.create_secret(
#     Name='DatabaseProdSecrets',
#     SecretString='{"username": "prod", "password": "hello-world-prod"}'
# )