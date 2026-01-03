from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DonationBase(BaseModel):
    full_amount: int
    comment: Optional[str] = None


class DonationDBBase(DonationBase):
    id: int
    create_date: datetime


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationDBBase):
    pass


class DonationFullInfoDb(DonationDBBase):
    invested_amount: int
    fully_invested: bool
    close_date: datetime = None
