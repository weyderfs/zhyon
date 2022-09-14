import boto3
from app.models.secret_model import Secret


client = boto3.client('secretsmanager')


def create_secret(secret: Secret):
    response = client.create_secret(
        Name = secret.name,
        ClientRequestToken = secret.client_request_token,
        Description = secret.description,
        KmsKeyId = secret.kms_key_id,
        SecretBinary = secret.secret_binary,
        SecretString = secret.secret_string,
        ForceOverwriteReplicaSecret = secret.force_overwrite_replica_secret,
        Tags = secret.tags,
        AddReplicaRegions = secret.replica_region
    )
    return {"arn": response.arn, "name": response.name}
