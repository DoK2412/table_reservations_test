from pydantic import BaseModel


class Table(BaseModel):
    id: int
    name: str
    seats: int
    location: str

    class Config:
        orm_mode = True
        from_attributes = True