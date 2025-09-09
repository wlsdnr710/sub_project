from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from backend.app.db.schema.user import UserCreate, UserUpdate
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
        #pydantic -> dict 
        db_user=User(**user.model_dump())
        #sqlalchemy -> pydantic모델 못받음 
        db.add(db_user) #insert into ~ 
        await db.commit()
        await db.refresh()
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



