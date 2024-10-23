from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

async def get_items(db: AsyncSession, model):
    query = select(model)
    result = await db.execute(query)  
    items = result.scalars().all()  
    return items

async def get_item(db: AsyncSession, item_id: int, model):
    query = select(model).filter(model.id == item_id)
    result = await db.execute(query)
    item = result.scalars().first()
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found"
        )
    return item