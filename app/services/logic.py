from datetime import datetime


def allocate(target, sources):
    target.invested_amount = target.invested_amount or 0
    for source in sources:
        if target.fully_invested:
            break

        remainder = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )

        for obj in (target, source):
            obj.invested_amount += remainder
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()
