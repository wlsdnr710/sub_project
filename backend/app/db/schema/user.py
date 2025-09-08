from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str
    username: str
    password: str
