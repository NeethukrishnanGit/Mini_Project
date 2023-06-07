from pydantic import BaseModel, Field
from enum import Enum
from fastapi import PydanticObjectId


class Roles(str, Enum):
    Employee = "Employee"
    Customer = "Customer"
    Partner = "Partner"


class User(BaseModel):
    id: PydanticObjectId = Field(..., alias='_id')
    User_Name: str = Field(...)
    Role: Roles = Field(...)
