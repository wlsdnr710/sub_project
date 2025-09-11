from pydantic import BaseModel, Field
from datetime import datetime, timezone

#pydantic 모델링 
#공통 필드
class UserBase(BaseModel):
    email:str
    username:str
    password:str

#회원가입
class UserCreate(UserBase):
    pass

#로그인
class UserLogin(BaseModel):
    email:str
    password:str

#수정
class UserUpdate(BaseModel):
    email:str|None=None
    username:str|None=None
    password:str|None=None


#DB에서 관리되는 모델
#기본값을 고정값이 아닌 함수 실행결과로 넣고싶을때: default_factory
class UserInDB(UserBase):  
    user_id:int
    created_at:datetime = Field(default_factory=lambda : datetime.now(timezone.utc))

    #sqlalchemy모델-> pydantic모델로 변환할때
    class Confing:
        from_attributes=True


#클라이언트에게 반환할 모델 -> UserInDB 그대로
class UserRead(UserInDB):
    pass