from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base
from app.models.base import BaseMixin


class Donation(Base, BaseMixin):
    comment: Mapped[str] = mapped_column(String, nullable=True)
