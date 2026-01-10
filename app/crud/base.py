from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.logic import allocate_donations


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get(self, object_id: int, session: AsyncSession):
        db_object = await session.execute(select(self.model).where(self.model.id == object_id))
        return db_object.scalars().first()

    async def create(self, object, session: AsyncSession):
        object_data = object.dict()
        db_object = self.model(**object_data)
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        await allocate_donations(session)
        await session.commit()
        return db_object

    async def update(self, db_object, object_in, session: AsyncSession):
        obj_data = jsonable_encoder(db_object)
        update_data = object_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def get_all(self, session: AsyncSession):
        objects = await session.execute(select(self.model))
        return objects.scalars().all()

    async def remove(self, object, session: AsyncSession):
        await session.delete(object)
        await session.commit()
        return object
