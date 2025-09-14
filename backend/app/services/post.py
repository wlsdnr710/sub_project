from sqlalchemy.ext.asyncio import AsyncSession
from app.db.scheme.posts import PostCreate, PostRead
from app.db.crud import PostCrud
from fastapi import HTTPException
from app.db.models import Posts


class PostService:
    @staticmethod
    async def create(db:AsyncSession, post_data:PostCreate, user_id:int):
        try:
            db_post=await PostCrud.create(db, post_data, user_id)

            await db.commit()
            await db.refresh(db_post)
            return db_post
        except Exception:
            raise

    @staticmethod
    async def get_id(db:AsyncSession, post_id:int, user_id:int):
        db_post=await PostCrud.get_id(db, post_id)

        if not db_post:
            raise HTTPException(status_code=404, detail="게시글 존재하지 않는다")
        return db_post
    
    
    @staticmethod
    async def get_all(db:AsyncSession, 
                    search:str|None=None,
                    category:str|None=None,
                    sort:str="created_at",
                    limit:int=10,
                    offset:int=0,
                    user_id:int|None=None):
        
        db_posts=await PostCrud.get_all_filter(db, search, category, sort, limit, offset)

        return db_posts
    
    @staticmethod
    async def count_total(db:AsyncSession, category:str|None, 
                          search:str|None):
        return await PostCrud.count_all(db, category, search)
    

    

    

