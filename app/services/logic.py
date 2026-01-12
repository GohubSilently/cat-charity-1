from datetime import datetime

from app.models import Fund


def allocate(
    target: Fund,
    sources: list[Fund],
) -> list[Fund]:
    update_source = []
    for source in sources:
        remainder = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )

        for obj in (target, source):
            obj.invested_amount += remainder
            update_source.append(obj)
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

        if target.fully_invested:
            break
    return update_source
