from pydantic import BaseModel, Field

from datetime import datetime


class Reservation(BaseModel):
    customer_name: str = Field(description="Имя бронирующего")
    table_id: int = Field(description="Номер бронируемого стола")
    reservation_time: datetime = Field(description="Дата брони стола")
    duration_minutes: int = Field(description="Минуты брони")