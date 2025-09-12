from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from jwt import ExpiredSignatureError, InvalidTokenError
from app.db.database import get_db
from app.core.jwt_context import verify_token, create_access_token, create_refresh_token
from app.db.crud import UserCrud
from app.core.auth import set_auth_cookies


#request-> Middleware -> call_next(request) -> 엔드포인트 -> response
#토큰 갱신 코드를 라우터마다 따로 넣으면 중복코드가 많아짐
#미들웨어에 넣음으로써 엔드포인트에서는 오직 비즈니스 로직만 구현하면됨
class TokenRefreshMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response= await call_next(request)  #요청 처리한 response객체 반환

        access_token=request.cookies.get("access_token")
        refresh_token=request.cookies.get("refresh_token")

        #토큰 검증 -> 리프레쉬토큰 발급받는 코드
        #InvalidTokenError -> pass해서 리프레시 토큰 확인으로 넘어감
        try:
            if access_token:
                verify_token(access_token)
                return response
        except InvalidTokenError:
            pass

        #리프레시 토큰 확인 -> 검증
        #예외나면 response반환할거임 (새 토큰 발급안함 - 로그아웃 상태)
        if refresh_token:
            try:
                user_id = verify_token(refresh_token)
            except (ExpiredSignatureError, InvalidTokenError):
                return response
            except (ExpiredSignatureError):
                return JSONResponse(
                    status_code=401,
                    content={"detail" : "refresh_token_expired"}
                )
            
            #새 토큰 발급(리프레시 토큰이 유효하다면 새 access_token,refresh_token 발급 )
            new_access_token=create_access_token(user_id)
            new_refresh_token=create_refresh_token(user_id)

            #anext : 비동기함수(비동기 제너레이터에서 yield값 꺼내는 함수)
            #db의 리프레시 토큰 업데이트
            try:
                db=await anext(get_db())
                await UserCrud.update_refresh_token_id(db, user_id, new_refresh_token)
                await db.commit()

            except Exception:
                raise

            set_auth_cookies(response, new_access_token, new_refresh_token)
        return response    









            


    




