from fastapi import Request, Response, HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError
from app.core.settings import settings
from app.core.jwt_context import verify_token
from typing import Optional


def set_auth_cookies(response: Response, access_token: str, refresh_token: str) -> None:
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="Lax",
        max_age=int(settings.access_token_expire.total_seconds()),
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="Lax",
        max_age=int(settings.refresh_token_expire.total_seconds()),
    )

    #요청객체에서 access_token꺼내서 
    #현재 로그인한 사용자 id가져오기 위해
async def get_user_id(request:Request):
    access_token=request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401)
        
    try:
        user_id=verify_token(access_token)
        if user_id is None:
            raise HTTPException(status_code=401)
        return user_id
    except InvalidTokenError:
        raise HTTPException(status_code=401)
    
#액세스 토큰이 없어도 예외던지지 않겠다. 그냥 None반환
#로그인 여부가 선택적인 api//로그인 안해도 볼수있는페이지에서 사용할때
async def get_user_id_option(request:Request):
    access_token=request.cookies.get("access_token")
    if not access_token:
        return None

    try:
        return verify_token(access_token)
    except InvalidTokenError:
        return None
    
        

