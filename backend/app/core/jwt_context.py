from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from app.core.settings import settings
import uuid


# bcrypt 는 해시 알고리즘 중 안정성이 높은편/ 패스워드 저장에 많이 쓴다
pwd_context = CryptContext(schemes=["bcrypt"])


# 해시값 저장
async def get_pwd_hash(password: str):
    return pwd_context.hash(password)


# 비번 검증(입력한 비번과. db에 저장된 해시값 비번 같으면 true)
async def verify_pwd(plain_password: str, hashed_pasword: str):
    return pwd_context.verify(plain_password, hashed_pasword)


def create_token(uid: int, expires_delta: timedelta, **kwargs) -> str:
    to_encode = kwargs.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire, "uid": uid})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.jwt_algo
    )
    return encoded_jwt


def create_access_token(uid: int) -> str:
    return create_token(uid=uid, expires_delta=settings.access_token_expire)


def create_refresh_token(uid: int) -> str:
    return create_token(
        uid=uid, jti=str(uuid.uuid4()), expires_delta=settings.refresh_token_expire
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.jwt_algo],
    )


def verify_token(token: str) -> int:
    payload = decode_token(token)
    return payload.get("uid")
