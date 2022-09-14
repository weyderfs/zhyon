from base64 import encode
from codecs import utf_8_encode
from fastapi import FastAPI
from app.models.secret_model import Secret
from app.services.secret_service import create_secret
# from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
   
@app.get("/healthz")
async def read_root():
   return {"PING": "200 OK - PONG"}

   # @app.post("/login/")
   # async def login(username: str = Form(), password: str = Form()):
   #    return {"username": username}

@app.post("/create-secret")
async def create_secret(secret: Secret):
   create_secret(secret)
