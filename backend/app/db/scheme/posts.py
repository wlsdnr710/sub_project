from pydantic import BaseModel, Field
from datetime import datetime, timezone


class PostBase(BaseModel):
    title: str
    desc: str
    category: str

class PostCreate(PostBase):
    pass


class PostInDB(PostBase):  
    post_id:int
    created_at:datetime = Field(default_factory=lambda : datetime.now(timezone.utc))
    user_id:int
    #sqlalchemy모델-> pydantic모델로 변환할때
    class Confing:
        from_attributes=True

class PostRead(PostInDB):
    pass