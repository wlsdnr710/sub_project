#db 폴더 및 models, crud, scheme 세개 폴더생성
#각 폴더에 user.py파일 생성
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func
from typing import Optional, List

#orm타입힌트 -> 새로운 타입 힌트방식 -> Mapped => 각필드의 특정타입을 좀 더 명확히 정의가능
class User(Base):
    __tablename__="users"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] =mapped_column(String(40), nullable=False)
    email: Mapped[str] =mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] =mapped_column(String(300), nullable=False)
    refresh_token:Mapped[Optional[str]] =mapped_column(String(300), nullable=True)
    created_at: Mapped[Optional[datetime]]= mapped_column(TIMESTAMP, server_default=func.now(), nullable=True)

    #1:M관계
    posts:Mapped[List["Posts"]]=relationship("Posts", back_populates="user", cascade="all, delete-orphan")
