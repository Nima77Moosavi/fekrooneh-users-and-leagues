from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DATE


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))

    xp: Mapped[int] = mapped_column(default=0)
    streak: Mapped[int] = mapped_column(default=0)
    max_streak: Mapped[int] = mapped_column(default=0)
    frozen_days: Mapped[int] = mapped_column(default=0)

    last_checkin: Mapped[date | None] = mapped_column(DATE, nullable=True)
    last_streak_reset: Mapped[date | None] = mapped_column(DATE, nullable=True)

    def __repr__(self) -> str:
        return f"<User(username={self.username}, xp={self.xp}, streak={self.streak})>"
