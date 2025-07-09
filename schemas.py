from pydantic import BaseModel , EmailStr

class User_model(BaseModel):
    id:int
    username:EmailStr
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


class Login_user(BaseModel):
    username:EmailStr
    password:str

    class Config:
        orm_mode = True
