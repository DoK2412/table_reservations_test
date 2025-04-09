from fastapi.responses import JSONResponse

from sqlalchemy import exc

from database.table_diagrams import Table

from .schemas import Table as ModelTable
from log.logger import logger


async def tables(db):
    try:
        all_table = db.query(Table).all()
        db.close()
        result_tables = [ModelTable.from_orm(table).dict() for table in all_table]
        logger.info("Запрос получения всего списка столов, выполнен успешно.")
        return JSONResponse(status_code=200,
                            content={"data": result_tables})
    except Exception as exc:
        logger.error(f"Получено исключение при исполнении кода {exc}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время получения столов произошла ошибка."})


async def create_new_table(table, db):
    try:
        check_table = db.query(Table).filter(Table.name == table.name).first()
        if check_table:
            logger.info(f"Ошибка: Попытка создать стол с существующим в базе именем {table.name}")
            return JSONResponse(status_code=400, content={"error": "Ошибка: Стол с таким именем уже существует."})
        add_table = Table(name=table.name, seats=table.seats,  location=table.location)
        db.add(add_table)
        db.commit()
        db.refresh(add_table)

        if add_table is not None:
            logger.info(f"Создан новый стол: id={add_table.id}, name={add_table.name}")
            return JSONResponse(status_code=200, content={"data": "Стол успешно создан."})
        else:
            return JSONResponse(status_code=400, content={"error": "Ошибка: Не удалось создать стол. Повторите попытку."})

    except Exception as exc:
        db.rollback()
        logger.error(f"Получено исключение при исполнении кода {exc}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время создания стола произошла ошибка."})
    finally:
        db.close()

async def delete_table(table_id, db):
    try:
        delete_tables = db.query(Table).filter(Table.id == table_id).first()
        if delete_tables is None:
            return JSONResponse(status_code=400, content={"error": "Ошибка: Не удалось удалить стол. Стол не найден."})
        else:
            db.delete(delete_tables)
            db.commit()
            return JSONResponse(status_code=200, content={"data": "Стол успешно удален."})
    except exc.IntegrityError:
        return JSONResponse(status_code=400, content={"error": "Ошибка: Невозможно удалить стол, возможно он зарезервирован. Проверьте брони стола."})
    except Exception as e:
        db.rollback()
        logger.error(f"Получено исключение при исполнении кода {e}")
        return JSONResponse(status_code=500, content={"error": "Ошибка: Во время удаления стола произошла ошибка."})
    finally:
        db.close()