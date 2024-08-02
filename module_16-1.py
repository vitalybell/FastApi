from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{id}")
async def user_id(id: int) -> str:
    return f"Вы вошли как пользователь № {id}"


@app.get('/user')
async def user_info(name: str, age: int) -> dict:
    return {'Информация о пользователе': f' Имя : {name},  Возраст: {age}'}
