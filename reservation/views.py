from fastapi.responses import JSONResponse

from datetime import datetime, timedelta
from sqlalchemy import exc
from database.table_diagrams import Reservation

from .schemas import Reservation as ModelReservation

from log.logger import logger


async def reservations(db):
    try:
        reservation = db.query(Reservation).all()
        db.close()
        result_reservation = list()
        for table in reservation:
            reserv = ModelReservation.from_orm(table)
            result_reservation.append({
                **reserv.dict(),
                'reservation_time': reserv.reservation_time.strftime('%Y-%m-%d %H:%M:%S')
            })
        logger.info("Запрос получения всех резервов столов выполнен успешно.")
        return JSONResponse(status_code=200,
                            content={"data": result_reservation})
    except Exception as e:
        logger.error(f"Получено исключение при исполнении кода {e}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время получения резерва столов произошла ошибка."})


async def create_reservation(db, reservation):
    try:
        check_reservation = db.query(Reservation).filter(Reservation.table_id == reservation.table_id).all()
        for reserv in check_reservation:
            if reserv.reservation_time <= reservation.reservation_time <= reserv.reservation_time + timedelta(minutes=reserv.duration_minutes):
                logger.info(f"Попытка создать бронь стола id={reserv.table_id} в зарезервированное ранее время {reservation.reservation_time}.")
                return JSONResponse(status_code=400, content={"error": "Ошибка: В указанное время стол уже зарезервирован."})

        create_reserv = Reservation(customer_name=reservation.customer_name,
                                    table_id=reservation.table_id,
                                    reservation_time=reservation.reservation_time,
                                    duration_minutes=reservation.duration_minutes,
                                    creation_date=datetime.now())
        db.add(create_reserv)
        db.commit()
        db.refresh(create_reserv)
        if create_reserv is not None:
            logger.info(f"Создана новая бронь: id={create_reserv.id}, time={create_reserv.reservation_time}, minutes={create_reserv.duration_minutes}")
            return JSONResponse(status_code=200, content={"data": "Бронь успешно создана."})
        else:
            return JSONResponse(status_code=400, content={"error": "Ошибка: Не удалось создать бронь. Повторите попытку."})

    except exc.IntegrityError:
        logger.info("Попытка создать бронь на несуществующий стол.")
        return JSONResponse(status_code=400, content={"error": "Ошибка: Указанного стола не существует. Проверьте столы."})

    except Exception as e:
        db.rollback()
        logger.error(f"Получено исключение при исполнении кода {e}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время создания резерва стола произошла ошибка."})
    finally:
        db.close()


async def del_reservations(db, reserv_id):
    try:
        delete_tables = db.query(Reservation).filter(Reservation.id == reserv_id).first()
        if delete_tables is None:
            logger.info("Попытка удалить несуществующую бронь.")
            return JSONResponse(status_code=400,
                                content={"error": "Ошибка: Не удалось удалить бронь. Проверьте ее наличие."})
        else:
            db.delete(delete_tables)
            db.commit()
            logger.info(f"Удалена бронь стола id={reserv_id}")
            return JSONResponse(status_code=200, content={"data": "Бронь успешно удалена."})
    except Exception as exc:
        db.rollback()
        logger.error(f"Получено исключение при исполнении кода {exc}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время удаления брони произошла ошибка."})
    finally:
        db.close()
