from datetime import datetime

from pydantic import BaseModel, validator


class CreateUser(BaseModel):
    name: str
    job: str
    id: int
    createdAt: datetime


class UpdateUser(BaseModel):
    name: str
    job: str
    updatedAt: datetime


class TypicalUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class ListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[TypicalUser] | list
    support: Support


class SingleUser(BaseModel):
    data: dict
    support: Support
