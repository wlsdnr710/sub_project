from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.user import UserCreate, UserUpdate
from sqlalchemy.future import select

#User와 관련된 CRUD 기능 클래스
class UserCrud:

    #user_id로 조회 -> select *from users where user_i =: id
    #결과가 1개면 객체 반환, 없으면 none
    @staticmethod
    async def get_id(db:AsyncSession, user_id:int) -> User | None:
        result=await db.execute(select(User).filter(User.user_id == user_id))
        return result.scalar_one_or_none()
    

    #생성
    @staticmethod
    async def create(db:AsyncSession, user:UserCreate) -> User :
        db_user=User(**user.model_dump())
        db.add(db_user)
        await db.flush()
        return db_user
    
    #삭제
    @staticmethod
    async def delete_by_id(db:AsyncSession, user_id:int):
        db_user=await db.get(User, user_id)
        if db_user:
            await db.delete(db_user)
            await db.flush() #db에 바로반영/ 롤백가능
            return db_user
        return None

    
    #username값 얻어오기(이름같은것만 필터링해서)
    @staticmethod
    async def get_username(db:AsyncSession, username:str):
        result=await db.execute(select(User).filter(User.username == username))
        return result.scalar_one_or_none()

    
    #email 값 얻어오기(이메일같으거 필터링)
    @staticmethod
    async def get_email(db:AsyncSession, email:str):
        result=await db.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()
    
    #수정
    @staticmethod
    async def update_by_id(db:AsyncSession, user_id:int, user:UserUpdate):
        db_user=await db.get(User, user_id)
        if db_user:
            #patch(요청에서 전달된 필드만 업데이트하겠다) {"email":"aa@naver.com"}
            update_user=user.model_dump(exclude_unset=True)
            for i, j in update_user.items():
                setattr(db_user, i, j)  #update
            await db.flush()
            return db_user
        return None
    


    #비동기 함수 -> await 사용/ db세션(db세션 함수에 await 붙임) 비동기 작업에 필요
    #user_id로 사용자 조회해서 존재하면 refresh_token필드 갱신하겠다
    @staticmethod
    async def update_refresh_token_id(
        db: AsyncSession, user_id: int, refresh_token: str
    ):
        db_user = await db.get(User, user_id)
        if db_user:
            db_user.refresh_token = refresh_token
            await db.flush()
        return db_user


