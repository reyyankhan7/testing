from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.get("/", response_model=list[schemas.BlogResponse])
def read_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)

@router.get("/{blog_id}", response_model=schemas.BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id)
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@router.post("/", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)

@router.put("/{blog_id}", response_model=schemas.BlogResponse)
def update_blog(blog_id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    updated_blog = crud.update_blog(db, blog_id, blog)
    if not updated_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog

@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    deleted_blog = crud.delete_blog(db, blog_id)
    if not deleted_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted"}

