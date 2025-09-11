from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey
from typing import Optional

#한명의 사용자가 여러개의 게시글을 등록할 수 있다.
class Posts(Base):
    __tablename__="posts"

    post_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] =mapped_column(String(300), nullable=False)
    desc: Mapped[str] =mapped_column(String(300), nullable=False)
    category: Mapped[str] =mapped_column(String(300), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    created_at: Mapped[Optional[datetime]]= mapped_column(TIMESTAMP, server_default=func.now(), nullable=True)

    #User객체와 관계설정 -> User모델에는 posts라는 역참조가 있어야한다
    user:Mapped["User"]=relationship("User",back_populates="posts")

   