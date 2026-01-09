from datetime import datetime

from pydantic import BaseModel, Field


class DonationCreate(BaseModel):
    full_amount: int = Field(gt=0)
    comment: str | None = None


class DonationDB(DonationCreate):
    id: int
    create_date: datetime


class DonationFullInfoDB(DonationDB, DonationCreate):
    invested_amount: int
    fully_invested: bool
    close_date: datetime | None = None
