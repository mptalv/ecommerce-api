from fastapi import FastAPI
from database import engine, Base

from routers import auth
from routers import users

from models.user import User 

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "E-Commerce API is running"}