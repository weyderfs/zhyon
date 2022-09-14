from fastapi import Depends, FastAPI, Form
from app.secret import Secret
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
   return secret.json()
