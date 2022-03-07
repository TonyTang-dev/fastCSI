from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Getin (BaseModel) :
    id : int
    name : str
    age : int
    passward : Optional[str] = None

class Findout(BaseModel) :
    id : int
    name : str
    age : int

@app.post("/api/loginByUnameAndPwd", response_model = Findout)
async def login(user : Getin) :
    json_compatible_data = jsonable_encoder(user)
    print(json_compatible_data)
    return user