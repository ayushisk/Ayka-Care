from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    owner_id: int
    class Config:
        from_attributes = True 

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    class Config:
         from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str