import datetime

from pydantic import BaseModel, Field


class CharityBase(BaseModel):
    name: str = Field(
        min_length=5,
        max_length=100,
    )
    description: str = Field(
        min_length=10,
    )
    full_amount: int = Field()



class CharityProjectDB(CharityBase):
    id: int
    invested_amount: int = Field()
    fully_invested: bool = Field(False)
    created_at: datetime
    close_date: datetime = Field(None)


class CharityProjectCreate(CharityBase):
    pass

class CharityProjectUpdate(CharityBase):
    pass
