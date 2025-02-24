from pydantic import BaseModel

from models.category import CategoryAdd


# class Category(SQLModel, table=True):
#     id: str = Field(default=None, primary_key=True)
#     name: str
#     username: str
#     archived: True
#
# class Spend(SQLModel, table=True):
#     id: str = Field(default=None, primary_key=True)
#     spendDate: str
#     category: Category=Relationship()
#     currency: str
#     amount: float
#     description: str
#     username: str | None = None


class SpendAdd(BaseModel):
    id: str | None = None
    spendDate: str
    currency: str
    amount: float
    description: str
    category: CategoryAdd
