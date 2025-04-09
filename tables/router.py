from fastapi import APIRouter, Depends, Query

from sqlalchemy.orm import Session


from .model_request import Table
from .views import tables, create_new_table, delete_table

from docs.docs import get_tables_responses, post_tables_responses, delete_tables_responses
from database.connection import get_db






table_router = APIRouter(prefix="/tables", tags=["tables"])

@table_router.get('/', responses=get_tables_responses)
async def get_tables(db: Session = Depends(get_db)):
    """Запрос просмотра существующих столов"""
    result = await tables(db)
    return result

@table_router.post('/', responses=post_tables_responses)
async def create_table(table: Table,
                       db: Session = Depends(get_db)):
    """Создание нового стола"""
    result = await create_new_table(table, db)
    return result

@table_router.delete('/', responses=delete_tables_responses)
async def delete_tables(id: int = Query(description="Id стола который необходимо удалить."),
                        db: Session = Depends(get_db)):
    """Удаление стола"""
    result = await delete_table(id, db)
    return result