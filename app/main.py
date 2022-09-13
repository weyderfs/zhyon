from fastapi import FastAPI, Form

app = FastAPI()

class Main():
   
   @app.get("/healthz")
   async def read_root():
      return {"PING": "200 OK - PONG"}

   @app.post("/login/")
   async def login(username: str = Form(), password: str = Form()):
      return {"username": username}


