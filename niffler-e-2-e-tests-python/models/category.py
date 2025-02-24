from pydantic import BaseModel


class CategoryAdd(BaseModel):
    id: str | None = None
    name: str
    username: str | None = None
    archived: bool | None = None
