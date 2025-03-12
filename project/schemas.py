from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True