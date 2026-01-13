from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import InvestmentInformation


class Donation(InvestmentInformation):
    comment: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        return f'{super().__repr__()}, comment={self.comment}'  # noqa: FCS100
