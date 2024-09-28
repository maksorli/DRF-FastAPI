from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI()

# Внешний API  (JSONPlaceholder)
EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com/users"


# Асинхронная функция для получения данных о пользователе с внешнего API
async def fetch_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL_API_URL}/{user_id}")
        if response.status_code == 200:
            return response.json()  # Возвращаем данные о пользователе в формате JSON
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching user data")


# Эндпоинт для получения данных о пользователе по его ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        user_data = await fetch_user_data(user_id)
        return user_data  # Возвращаем данные клиенту
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=response.status_code, detail="Error fetching user data")
    

# Эндпоинт для получения пользователя по имени или email
@app.get("/users/search/")

async def search_user(name: str = Query(None), email: str = Query(None)):
    async with httpx.AsyncClient() as client:
        response = await client.get(EXTERNAL_API_URL)
        if response.status_code == 200:
            users = response.json()
            # Фильтруем пользователей по имени или email
            if name:
                users = [user for user in users if user['name'].lower() == name.lower()]
            if email:
                users = [user for user in users if user['email'].lower() == email.lower()]
                
            if not users:
                raise HTTPException(status_code=404, detail="User not found")
            return users  # Возвращаем найденных пользователей
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching user data")
