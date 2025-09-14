from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Posts
from app.db.scheme.posts import PostCreate
from sqlalchemy.future import select
from sqlalchemy import or_ , desc, func


class PostCrud:
    
    @staticmethod
    async def create(db:AsyncSession, post_data:PostCreate, user_id:int):
        post_dict=post_data.model_dump()
        post_dict["user_id"]=user_id
        new_post=Posts(**post_dict)
        db.add(new_post)
        await db.flush()
        return new_post


    @staticmethod
    async def get_id(db:AsyncSession, post_id:int):
        return await db.get(Posts, post_id)


    @staticmethod
    async def delete_id(db:AsyncSession, post_id:int):
        post=await db.get(Posts, post_id)
        if post:
            await db.delete(post)
            await db.flush()
            return True
        return False
    
    
    @staticmethod
    async def get_all_filter(db:AsyncSession, 
                             search:str|None=None,
                             category:str|None=None,
                             sort:str="created_at",
                             limit:int=10,
                             offset:int=0):
        query=select(Posts) #select *from Posts 

        if search:
            query=query.where(or_(Posts.title.ilike(f"%{search}%"),
                                  Posts.desc.ilike(f"%{search}%")))
            
        if category:
            query=query.where(Posts.category==category) #select *from Posts where Posts.category==category
        
        if sort=="created_at":
            query=query.order_by(desc(Posts.created_at))


        query=query.limit(limit).offset(offset)
        result=await db.execute(query)
        return result.scalars().all() #쿼리결과에서 하나만 추출해서 그 정보를 리스트로 추출
    

    @staticmethod
    async def count_user_id(db:AsyncSession, user_id:int):
        result=await db.execute(select(func.count()).where(Posts.user_id==user_id ))
        return result.scalar() or 0 #None이거나 0이면 return 0
    
    @staticmethod
    async def count_all(db:AsyncSession, category:str|None=None, search:str|None=None):
        query=select(func.count()).select_from(Posts)

        if category:
            query=query.where(Posts.category==category)
        
        if search:
            query=query.where(Posts.title.ilike(f"%{search}")) | (Posts.desc.ilike(f"%{search}"))


        result=await db.execute(query)
        return result.scalar() or 0 