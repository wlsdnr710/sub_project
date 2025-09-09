from pydantic import BaseModel, Field
from datetime import datetime, timezone


class UserBase(BaseModel):
    email: str
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None


# DB 에서 고나리되는 모델
class UserInDB(UserBase):
    user_id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # sqlahcemy 모델 -> pydantic 모델로 변환
    class Config:
        from_attribute = True


class UserRead(UserInDB):
    pass
