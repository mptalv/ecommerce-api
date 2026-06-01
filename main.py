from fastapi import FastAPI
from database import engine, Base

from user import User 

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "E-Commerce API is running"}