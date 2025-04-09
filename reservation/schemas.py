from pydantic import BaseModel

from datetime import datetime


class Reservation(BaseModel):
    id: int
    table_id: int
    customer_name: str
    reservation_time: datetime
    duration_minutes: int

    class Config:
        orm_mode = True
        from_attributes = True