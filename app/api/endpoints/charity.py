from datetime import datetime
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_project_exists, check_unique_name, check_full_amount
)
from app.core.db import get_async_session
from app.crud.charity import charity_crud
from app.schemas.charity import (
    CharityProjectCreate, CharityProjectDB, CharityProjectUpdate
)


router = APIRouter()
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    description='Показать список всех целевых проектов.',
    response_model_exclude_none=True
)
async def get_all_charity_projects(
    session: SessionDep
):
    return await charity_crud.get_all(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    description='Создать целевой проект.',
    response_model_exclude_none=True,
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: SessionDep
):
    await check_unique_name(charity_project.name, session)
    return await charity_crud.create(charity_project, session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    description='Редактировать целевой проект.',
    response_model_exclude_none=True
)
async def update_charity_project(
    project_id: int,
    charity_project: CharityProjectUpdate,
    session: SessionDep,
):
    charity = await check_charity_project_exists(project_id, session)
    await check_unique_name(charity_project.name, session)
    if charity.fully_invested is True:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя удалить!'
        )
    charity = await check_full_amount(charity.id, charity_project.full_amount, session)
    if charity.invested_amount == charity_project.full_amount:
        charity.fully_invested = True
        charity.close_date = datetime.now()
    return await charity_crud.update(charity, charity_project, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    description='Удалить целевой проект.',
    response_model_exclude_none=True
)
async def delete_charity_project(
    project_id: int,
    session: SessionDep
):
    charity_project = await check_charity_project_exists(project_id, session)
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return await charity_crud.remove(charity_project, session)
