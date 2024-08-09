from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_user(request: Request,
                   user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{username}/{age}')
async def add_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    try:
        idx = [user.id for user in users].index(user_id)
        users[idx].username = username
        users[idx].age = age
        return users[idx]
    except ValueError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> User:
    try:
        idx = [user.id for user in users].index(user_id)
        user = users.pop(idx)
        return user
    except ValueError:
        raise HTTPException(status_code=404, detail='User was not found')
