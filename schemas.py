from pydantic import BaseModel

class User_model(BaseModel):
    id:int
    username:str
    password:str

    class Config:
        orm_mode = True

class Note_model(BaseModel):
    id:int
    title:str
    content:str
    owner_id:int

    class Config:
        orm_mode = True

