from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Posts
from app.db.scheme.posts import PostCreate, PostRead
from app.services import PostService
from app.db.database import get_db
from app.core.auth import get_user_id, get_user_id_option

router=APIRouter(prefix="/posts", tags=["Post"])

#로그인을 한 이후에 게시글작성.. (로그인 된 사용자의 )- 누가 게시글을 작성했는지
@router.post("/",response_model=PostRead)
async def create_post(
    post_data:PostCreate,
    user_id:int=Depends(get_user_id),
    db:AsyncSession=Depends(get_db)):
    
    return await PostService.create(db, post_data, user_id)


@router.get("/", response_model=list[PostRead])
async def list_posts(
    db: AsyncSession=Depends(get_db),
    user_id: int|None=Depends(get_user_id_option),
    search: str|None=Query(None, min_length=1),
    category: str|None=Query(None),
    sort:str=Query("created_at", enum=["created_at","like_count","review_count"]),
    limit:int = Query(10, ge=1, le=50),
    offset:int = Query(0,ge=0)
):
    return await PostService.get_all(
        db=db,
        search=search,
        category=category,
        sort=sort,
        limit=limit,
        offset=offset,
        user_id=user_id
    )

    
@router.get("/count", response_model=int)
async def count_posts(
    db:AsyncSession=Depends(get_db),
    search: str|None=Query(None, min_length=1),
     category: str|None=Query(None)):
    
    return await PostService.count_total(db, category, search)