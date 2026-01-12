from app.models import InvestmentInformation


def allocate(
    target: InvestmentInformation,
    sources: list[InvestmentInformation],
) -> list[InvestmentInformation]:
    update_sources = []
    for source in sources:
        remainder = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        target.invested_amount += remainder
        source.invested_amount += remainder
        for obj in (target, source):
            if obj.invested_amount == obj.full_amount:
                obj.close_fund()
        if source not in update_sources:
            update_sources.append(source)
        if target.fully_invested:
            break
    return update_sources
