from fastapi import FastAPI
from database import Base, engine
import models
from routers import blog

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Blog API")
app.include_router(blog.router)
