from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity import charity_crud


async def check_unique_name(
    name: str,
    session: AsyncSession
):
    charity_project = await charity_crud.get_name(name, session)
    if charity_project is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!'
        )
    return charity_project


async def check_full_amount(
    charity_project_id: int,
    full_amount: int,
    session: AsyncSession
):
    charity_project = await check_charity_project_exists(charity_project_id, session)
    if full_amount >  charity_project.full_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Нельзя установить значение full_amount мнеьше уже вложенной суммы.'
        )
    return charity_project



async def check_charity_project_exists(
    charity_project_id: int,
    session: AsyncSession,
):
    charity_project = await charity_crud.get(charity_project_id, session)
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Благотворительного проекта не существует!',
        )
    return charity_project