from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.engine import Base


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    repositories: Mapped[List["Repository"]] = relationship(back_populates="owner")
    is_active: Mapped[bool] = mapped_column(default=True)


class Repository(Base):
    __tablename__ = "repository_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    updated_at: Mapped[datetime] = mapped_column(default=func.now(), onupdate=func.now)
    owner_id: Mapped[int] = mapped_column(ForeignKey("owners.id"))
    owner: Mapped["User"] = relationship(back_populates="repositories")
    file_id: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
