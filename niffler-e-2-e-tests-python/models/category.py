from pydantic import BaseModel
# from sqlmodel import SQLModel, Field


class CategoryAdd(BaseModel):
    id: str | None = None
    name: str
    username: str | None = None
    archived: bool | None = None


# class Category(SQLModel, table=True):
#     id: str = Field(default=None, primary_key=True)
#     name: str
#     username: str
#     archived: True
