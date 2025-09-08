from pydantic_settings import BaseSettings
from pydantic import Field

# fastapi 에서 설정 관리할때 자주 사용
# 환경변수에서 값을 자동으로 불러 올 수 있는 클래스


class Settings(BaseSettings):
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")
    db_host: str = Field("localhost", alias="DB_HOST")
    db_port: str = Field("3306", alias="DB_PORT")
    db_name: str = Field(..., alias="DB_NAME")

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"
        populate_by_name = True

    @property
    def tmp_db(self) -> str:  # "root:12345@localhost:3306/board"
        return f"{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property  # 비동기 DB URL
    def db_url(self) -> str:  # "mysql+asyncmy://root:12345@localhost:3306/board"
        return f"mysql+asyncmy://{self.tmp_db}"

    @property  # 동기 DB URL
    def sync_db_url(self) -> str:
        return f"mysql+pymysql://{self.tmp_db}"


# 전역 설정
settings = Settings()
