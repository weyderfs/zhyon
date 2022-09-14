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
        Name=secret.name,
        ClientRequestToken=secret.client_request_token,
        Description=secret.description,
        KmsKeyId=secret.kms_key_id,
        SecretBinary=secret.secret_binary,
        SecretString=secret.secret_string,
        ForceOverwriteReplicaSecret=secret.force_overwrite_replica_secret,
        Tags=secret.tags,
        AddReplicaRegions=secret.replica_regions
    )
    return {"arn": response.arn, "name": response.name}

