import pytest
from fastapi.testclient import TestClient
from main import app  # assuming the FastAPI app is in a file named main.py

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_user_by_id():
    # тест ID
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

@pytest.mark.asyncio
async def test_get_user_by_id_not_found():
    # Тест несуществуюшего id
    response = client.get("/users/1000")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@pytest.mark.asyncio
async def test_search_user_by_name():
    # Тест поиск  по имени
    response = client.get("/users/search/?name=Leanne Graham")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Leanne Graham"

@pytest.mark.asyncio
async def test_search_user_by_email():
    # Тест поиск по почте
    response = client.get("/users/search/?email=Sincere@april.biz")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["email"] == "Sincere@april.biz"

@pytest.mark.asyncio
async def test_search_user_by_name_and_email():
    # Тест поиск по имени и почте
    response = client.get("/users/search/?name=Leanne Graham&email=Sincere@april.biz")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Leanne Graham"
    assert response.json()[0]["email"] == "Sincere@april.biz"

@pytest.mark.asyncio
async def test_search_user_not_found():
    # Тест несуществуюшего пользователя
    response = client.get("/users/search/?name=Unknown User")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"