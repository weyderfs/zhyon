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
    description: Optional[str | None]
    secret_string: Optional[str | None]

    class Config:
        schema_extra = {
            "example": {
                "name": "acabate-db",
                "description": "Abacate é uma fruta, mas também é a secret do DB",
                "secret_string": "batatinhaquandonasce"
            }
        }
