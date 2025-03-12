from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List

from models import Base, User
from database import engine, session_local
from schemas import UserBase, User as DBUser

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def get_main_page1():
    with open("main.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())


@app.get("/enter", response_class=HTMLResponse)
async def get_login_page2():
    with open("enter.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())


@app.post("/enter", response_model=DBUser)
async def login(name: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)) -> DBUser:
    user_data = UserBase(name=name, password=password)
    db_user = User(name=user_data.name, password=user_data.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/enter/", response_model=List[DBUser])
async def posts(db: Session = Depends(get_db)):
    return db.query(User).all()
