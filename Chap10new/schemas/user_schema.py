from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRegister(BaseModel):
    username: str
    password: str


class UsernameRequest(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    dta: str
    user: UserResponse