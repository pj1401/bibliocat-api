"""
User models.
module: src/util/models/user.py
"""

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr


class UserArguments(User):
    password: str = Field(..., min_length=8)


class UserModel(BaseModel):
    __tablename__: str = "users"
    user_id: int
    username: str
    email: EmailStr
    password_hash: str
    permission_level: int
