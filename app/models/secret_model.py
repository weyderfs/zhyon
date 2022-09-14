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
  client_request_token: Optional[str]
  description: Optional[str]
  kms_key_id: Optional[str]
  secret_binary: Optional[str]
  secret_string: Optional[str]
  force_overwrite_replica_secret: Optional[bool]
  tags: Optional[List[Tag]]
  replica_regions: Optional[List[ReplicaRegion]]

  
  class Config:
    schema_extra = {
      "example": {
        "name": "acabate-db",
        "description": "Abacate é uma fruta, mas também é a secret do DB",
        "secret_string": "batatinhaquandonasce"
      }
    }
 