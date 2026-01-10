from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def allocate_donations(session: AsyncSession):
    charity_project_objects = await session.execute(
        select(
            CharityProject
        ).where(
            CharityProject.fully_invested is False
        ).order_by(
            CharityProject.create_date
        )
    )
    donation_objects = await session.execute(
        select(
            Donation
        ).where(
            Donation.fully_invested is False
        ).order_by(
            Donation.create_date
        )
    )
    charity_projects = charity_project_objects.scalars().all()
    donations = donation_objects.scalars().all()
    if donations:
        for donation in donations:
            for charity in charity_projects:
                remainder = min(
                    charity.full_amount - charity.invested_amount,
                    donation.full_amount - donation.invested_amount
                )
                donation.invested_amount += remainder
                charity.invested_amount += remainder
                if charity.invested_amount == charity.full_amount:
                    charity.fully_invested = True
                    charity.close_date = datetime.now()
                if donation.invested_amount == donation.full_amount:
                    donation.fully_invested = True
                    donation.close_date = datetime.now()
