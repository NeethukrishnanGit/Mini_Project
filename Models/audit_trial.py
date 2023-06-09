from pydantic import BaseModel, Field
from datetime import datetime


class Audit(BaseModel):
    user_id: str = Field(...)
    instrument_id: str = Field(...)
    event_type: str = Field(...)
    time: str = Field(default=datetime.utcnow())
