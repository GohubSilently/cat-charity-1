from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base, CommonMixin


class CharityProject(CommonMixin, Base):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String)
