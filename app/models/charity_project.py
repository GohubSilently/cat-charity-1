from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import FundMixin


class CharityProject(FundMixin):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        base = super().__repr__()
        return (f'{base}, id={self.id}, name={self.name}, '
                f'create_date={self.create_date}')
