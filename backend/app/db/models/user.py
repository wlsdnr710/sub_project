from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func
from typing import Optional


# orm type hint -> 새로운 힌트 방식 (Mapped)
class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(40), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=True
    )
