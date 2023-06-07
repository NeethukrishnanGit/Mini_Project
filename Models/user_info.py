from pydantic import BaseModel, Field
from enum import Enum


class Roles(str, Enum):
    Employee = "Employee"
    Customer = "Customer"
    Partner = "Partner"


class User(BaseModel):
    User_Name: str = Field(...)
    Role: Roles = Field(...)
