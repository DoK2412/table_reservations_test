from pydantic import BaseModel, Field


class Table(BaseModel):
    name: str = Field(description="Наименование стола")
    seats: int = Field(description="Количество мест за столом")
    location: str = Field(description="Место нахождения стола зале")
