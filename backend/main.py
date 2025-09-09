import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, async_engine
from fastapi.concurrency import asynccontextmanager
from app.db.models import user

#애플리케이션의 시작과 종료 시 실행될 작업을 정의함
#시작/끝을 비동기적으로 처리
@asynccontextmanager
async def lifespan(app:FastAPI):
    async with async_engine.begin() as conn: #DB 연결 시작하고
        await conn.run_sync(Base.metadata.create_all) #정의된 테이블 모두 생성
    yield #앱 실행 중단하고 나머지 코드는 앱이 종료될 때 실행하겠다
    await async_engine.dispose() #DB 연결 종료


#앱 시작과 종료시 DB테이블 생성 및 엔진 종료 작업 실행하겠다
app=FastAPI(lifespan=lifespan)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #모든 도메인요청 허용
    allow_credentials=True, #자격증명 true일경우에만 응답 노출
    allow_methods=["*"], #모든 http메소드 허용
    allow_headers=["*"],

)

# if __name__=="__main__":
#     uvicorn.run("main:app",host="localhost",port=8081,reload=True)