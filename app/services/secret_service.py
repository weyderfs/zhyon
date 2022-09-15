import boto3
from app.models.secret_model import Secret
from logging.config import dictConfig
import logging
from app.logconfig import LogConfig


dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

client = boto3.client('secretsmanager')

def create_secret_service(secret: Secret):
    logger.info("logging from the create secret service")
    response = client.create_secret(
      Name='secret.name',
      Description='secret.description',
      SecretString='secret.secret_string'
    )
    return response
