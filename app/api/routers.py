from fastapi import APIRouter

from app.api.endpoints import charity_router, donation_router


main_router = APIRouter()
main_router.include_router(
    charity_router, prefix='/charity-project', tags=['charity_projects']
)
main_router.include_router(
    donation_router, prefix='/donation', tags=['donations']
)
