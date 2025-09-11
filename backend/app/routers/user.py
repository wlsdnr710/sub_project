from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.user import UserCreate, UserUpdate, UserLogin, UserRead
from app.services import UserService
from app.db.database import get_db
from app.core.auth import set_auth_cookies, get_user_id


# scheme(user.py) / crud -> serivce -> router(contoller) -> front

router=APIRouter(prefix="/users", tags=["User"])

#기본값이 없는 매개변수는 기본값이 있는 매개변수보다 앞에 와야한다

@router.post("/signup", response_model= UserRead)
async def signup(user:UserCreate, db:AsyncSession=Depends(get_db)):
    db_user=await UserService.signup(db, user)
    return db_user


@router.post("/login", response_model=UserRead)
async def login(user: UserLogin,response: Response, db: AsyncSession = Depends(get_db)):
    result = await UserService.login(db, user)
    db_user, access_token, refresh_token = result
    set_auth_cookies(response, access_token, refresh_token)
    return db_user

@router.post("/logout", response_model=bool)
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return True

#쿠키에서 access_token 꺼내서 로그인한 사용자의 user_id 를 매개변수 user_id에 주입
@router.get("/userme", response_model=UserRead)
async def get_user(user_id:int = Depends(get_user_id), db:AsyncSession=Depends(get_db)):
    return await UserService.get_user(db, user_id)
