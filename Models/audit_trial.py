from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime



class Status(str, Enum):
    Check_out = "Check Out"
    Check_in = "Check In"


class Audit(BaseModel):
    user_id: str = Field(...)
    instrument_id: str = Field(...)
    Event_Type: Status = Field(...)
    Date_Time: str = Field(default=datetime.utcnow())

