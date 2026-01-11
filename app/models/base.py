from datetime import datetime

from sqlalchemy import Integer, Boolean, DateTime, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class FundMixin(Base):
    __abstract__ = True

    full_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    invested_amount: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False
    )
    fully_invested: Mapped[bool] = mapped_column(Boolean, default=False)
    create_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now
    )
    close_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint('full_amount > 0'),
    )
