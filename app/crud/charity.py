from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharity(CRUDBase):
    async def get_name(
        self,
        name: str,
        session: AsyncSession
    ):
        db_object = await session.execute(select(self.model).where(
            self.model.name == name)
        )
        return db_object.scalars().first()

    async def get_charity(
        self,
        session: AsyncSession
    ):
        statement = select(self.model).order_by(
            desc(self.model.fully_invested),
            desc(self.model.created_date)
        )
        db_object = await session.execute(statement)
        return db_object.scalars().first()


charity_crud = CRUDCharity(CharityProject)
