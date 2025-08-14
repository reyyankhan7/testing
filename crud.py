from sqlalchemy.orm import Session
import models, schemas

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db.commit()
        db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog
