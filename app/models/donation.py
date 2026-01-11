from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import FundMixin


class Donation(FundMixin):
    comment: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        base = super().__repr__()
        return (f'{base}, id={self.id}, comment={self.comment}, '
                f'create_date={self.create_date}')
