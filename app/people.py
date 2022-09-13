from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class People(BaseModel):
   id: int
   name: str
   email: str
   enterprise: str
   job_position: str

  @app.get("/person")
  async def get_person():
      return person

  @app.get("/person/{person_id}")
  async def get_person_by_id(person_id):
      return {"person_id": person_id}


  @app.put("/person/{person_id}")
  async def update_person(person_id: int, person: People):
    return {"person_name": person.name, "person_id": person_id}

  @app.post("/person")
  async def create_person(person: People):
      return person