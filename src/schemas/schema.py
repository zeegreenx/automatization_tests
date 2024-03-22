from datetime import datetime

from pydantic import BaseModel, field_validator


class CreateUser(BaseModel):
    name: str
    job: str
    id: int
    createdAt: datetime


class UpdateUser(BaseModel):
    name: str
    job: str
    updatedAt: datetime


class UpdField(BaseModel):
    name: str = 'test-case'


class TypicalUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator('first_name', 'last_name', 'email', 'avatar')
    def fields_shouldnt_exist_space(cls, value, info):
        if ' ' in value:
            raise ValueError(f"{info.name} should not contain spaces")
        return value


class Support(BaseModel):
    url: str = "https://reqres.in/#support-heading"
    text: str = "To keep ReqRes free, contributions towards server costs are appreciated!"


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


first_page = ListUsers(
    page=1,
    per_page=6,
    total=12,
    total_pages=2,
    data=[
        TypicalUser(id=1, email='george.bluth@reqres.in', first_name='George', last_name='Bluth',
                    avatar='https://reqres.in/img/faces/1-image.jpg'),
        TypicalUser(id=2, email='janet.weaver@reqres.in', first_name='Janet', last_name='Weaver',
                    avatar='https://reqres.in/img/faces/2-image.jpg'),
        TypicalUser(id=3, email='emma.wong@reqres.in', first_name='Emma', last_name='Wong',
                    avatar='https://reqres.in/img/faces/3-image.jpg'),
        TypicalUser(id=4, email='eve.holt@reqres.in', first_name='Eve', last_name='Holt',
                    avatar='https://reqres.in/img/faces/4-image.jpg'),
        TypicalUser(id=5, email='charles.morris@reqres.in', first_name='Charles', last_name='Morris',
                    avatar='https://reqres.in/img/faces/5-image.jpg'),
        TypicalUser(id=6, email='tracey.ramos@reqres.in', first_name='Tracey', last_name='Ramos',
                    avatar='https://reqres.in/img/faces/6-image.jpg'),
    ],
    support=Support(
        url="https://reqres.in/#support-heading",
        text="To keep ReqRes free, contributions towards server costs are appreciated!"
    )
)

empty_page = ListUsers(
    page=200,
    per_page=6,
    total=12,
    total_pages=2,
    data=[],
    support=Support(
        url="https://reqres.in/#support-heading",
        text="To keep ReqRes free, contributions towards server costs are appreciated!"
    )
)
