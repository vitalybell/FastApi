from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{id}")
async def user_id(id: Annotated[int, Path(ge=1, le=100, description="Введите свой ID", exemple=1)]) -> str:
    return f"Вы вошли как пользователь № {id}"


@app.get('/user')
async def user_info(name: str, age: int) -> dict:
    return {'Информация о пользователе': f' Имя : {name},  Возраст: {age}'}


@app.get("/user/{username}/{age}")
async def enter_user_id(username: Annotated[str, Path(min_length=5, max_length=20
    ,description="Введите ваше имя", exemple="Виталий")]
    ,age: Annotated[int, Path(ge=18, le=100, description="Введите свой возраст", exemple=45)]) -> dict:
    return {"User": username, "Age": age}