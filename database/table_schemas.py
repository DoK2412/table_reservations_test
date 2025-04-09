from pydantic import BaseModel

from datetime import datetime

class Table(BaseModel):
    id: int
    name: str
    seats: int
    location: str

class Reservation(BaseModel):
    id: int
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int