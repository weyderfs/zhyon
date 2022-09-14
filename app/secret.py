from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Secret(BaseModel):
  name = str
  clientrequesttoken = str
  description = str
  kmskeyid = str
  secretbinary = str,
  secretstring = str,
  ForceOverwriteReplicaSecret = bool

class Tag(BaseModel):
  key = str
  value = str

class ReplicaRegion(BaseModel):
  region = str
  kmskeyid = str