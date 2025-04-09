from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from .views import create_reservation, reservations, del_reservations
from .model_request import Reservation

from docs.docs import get_reservations_responses, post_reservations_responses, delete_reservations_responses
from database.connection import get_db



router_reservations = APIRouter(prefix="/reservations", tags=["reservations"])


@router_reservations.get('/', responses=get_reservations_responses)
async def get_reservations(db: Session = Depends(get_db)):
    """Запрос просмотра всех броней"""
    result = await reservations(db)
    return result

@router_reservations.post('/', responses=post_reservations_responses)
async def post_create_reservation(reservation: Reservation,
                             db: Session = Depends(get_db)
                             ):
    """Запрос создания брони"""
    result = await create_reservation(db, reservation)
    return result

@router_reservations.delete('/', responses=delete_reservations_responses)
async def delete_reservation(id: int,
                             db: Session = Depends(get_db)
                             ):
    """Запрос удаления брони"""
    result = await del_reservations(db, id)
    return result