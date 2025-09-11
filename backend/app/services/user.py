# scheme(user.py) / crud -> serivce -> router(contoller) -> front
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.scheme.user import UserCreate, UserLogin
from app.db.crud import UserCrud
from fastapi import HTTPException
from app.core.jwt_context import get_pwd_hash, verify_pwd, create_access_token, create_refresh_token

class UserService:

    #DB에서 해당 id의 사용자 조회 
    @staticmethod
    async def get_user(db:AsyncSession, user_id:int):
        db_user=await UserCrud.get_id(db, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="사용자 찾을 수 없다")
        return db_user


    @staticmethod
    async def signup(db:AsyncSession, user:UserCreate):
        #중복 username확인
        if await UserCrud.get_username(db, user.username):
            raise HTTPException(status_code=400,  detail="이미 사용중인 이름이다")
        
        #username없으면 -> username, password, email을 디비에 저장해야함
        hash_pw=await get_pwd_hash(user.password) #비번 암호화해서 들어감
        user_create=UserCreate(username=user.username, password=hash_pw, email=user.email)

        try:
            db_user=await UserCrud.create(db,user_create)
            await db.commit()
            await db.refresh(db_user)
            return db_user
        
        except Exception:
            raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비번이다")



    @staticmethod
    async def login(db: AsyncSession, user: UserLogin) -> tuple:
        db_user = await UserCrud.get_email(db, user.email)
        if not db_user or not await verify_pwd(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비밀번호")
        

        refresh_token = create_refresh_token(db_user.user_id)
        access_token = create_access_token(db_user.user_id)

        updated_user = await UserCrud.update_refresh_token_id(db, db_user.user_id, refresh_token)
        await db.commit()
        await db.refresh(updated_user)

        return updated_user, access_token, refresh_token





        
    
 