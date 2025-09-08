import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, async_engine
from fastapi.concurrency import asynccontextmanager


# 앱 시작과 종료시 실행될 작업을 정의함.
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:  # DB 연결 시작
        await conn.run_sync(Base.metadata.create_all)  # 정의된 테이블 모두 생성
    yield  # 앱이 종료될때 실행
    await async_engine.dispose()  # DB 연결 종료료


# 앱 시작과 종료시 DB 테이블 생성 및 엔진 종료 작업 실행하겠다.
app = FastAPI(lifespan=lifespan)


# cors 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=True)
