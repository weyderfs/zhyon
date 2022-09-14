from base64 import encode
from codecs import utf_8_encode
from fastapi import FastAPI
from app.models.secret_model import Secret
from app.services.secret_service import create_secret_service
from logging.config import dictConfig
import logging
from app.logconfig import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

logger.info("Dummy Info")
logger.error("Dummy Error")
logger.debug("Dummy Debug")
logger.warning("Dummy Warning")


app = FastAPI()


## Health Check Route
@app.get("/healthz")
async def read_root():
    return {"PING": "200 OK - PONG"}


# Route to create secret at AWS Secret Manager /services/secret_service.py
@app.post("/create-secret")
async def create_secret(secret: Secret):
    logger.info("logging from the create secret")
    response = create_secret_service(secret)
    return response
