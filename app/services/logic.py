from datetime import datetime
from typing import Union, List

from app.models import CharityProject, Donation


def allocate(
    target: Union[CharityProject, Donation],
    sources: List[Union[CharityProject, Donation]],
) -> List[Union[CharityProject, Donation]]:
    for source in sources:
        # Для тестов. Они передают None, в БД сделал так
        # чтобы None не могло быть.
        if target.invested_amount is None:
            target.invested_amount = 0
        remainder = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )

        for obj in (target, source):
            obj.invested_amount += remainder
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

        if target.fully_invested:
            break
    return sources