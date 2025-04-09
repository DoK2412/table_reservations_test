import os


import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tables.router import table_router
from reservation.router import router_reservations

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title='Сервис бронирования столиков',
    version='0.0.1')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(table_router)
app.include_router(router_reservations)


if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))