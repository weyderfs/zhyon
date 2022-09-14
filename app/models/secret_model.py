from typing import Optional, List
from pydantic import BaseModel


class Tag(BaseModel):
    key = str
    value = str


class ReplicaRegion(BaseModel):
    region = str
    kms_key_id = str


class Secret(BaseModel):
    name: str
    client_request_token: Optional[str | None]
    description: Optional[str | None]
    kms_key_id: Optional[str | None]
    secret_binary: Optional[str | None]
    secret_string: str
    force_overwrite_replica_secret: Optional[bool | None]
    tags: Optional[List[Tag] | None]
    replica_regions: Optional[List[ReplicaRegion] | None]

    class Config:
        schema_extra = {
            "example": {
                "name": "acabate-db",
                "description": "Abacate é uma fruta, mas também é a secret do DB",
                "secret_string": "batatinhaquandonasce"
            }
        }
