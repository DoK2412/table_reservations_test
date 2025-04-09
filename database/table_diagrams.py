from dotenv import load_dotenv

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP


from database.connection import Base, engine

load_dotenv()

class Table(Base):
    __tablename__ = 'table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String, nullable=False)


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    table_id = Column(Integer, ForeignKey("table.id"))
    reservation_time = Column(TIMESTAMP, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)


Base.metadata.create_all(engine)
