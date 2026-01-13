from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity import charity_crud
from app.crud.donation import donation_crud
from app.services.logic import allocate
from app.schemas.donation import DonationCreate, DonationDB, DonationFullInfoDB


router = APIRouter()


SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
    '/',
    response_model=list[DonationFullInfoDB],
    description='Показать список всех пожертвований.',
    response_model_exclude_none=True
)
async def get_all_donations(
    session: SessionDep
):
    return await donation_crud.get_all(session)


@router.post(
    '/',
    response_model=DonationDB,
    description='Создать пожертвование.',
    response_model_exclude_none=True
)
async def create_donation(
    donation: DonationCreate,
    session: SessionDep,
):
    donation = await donation_crud.create(donation, session, commit=False)
    session.add_all(allocate(
        donation, await charity_crud.get_not_fully_invested(session)
    ))
    await session.commit()
    await session.refresh(donation)
    return donation
