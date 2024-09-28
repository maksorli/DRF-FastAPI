# Simple DRF
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-5.1.1-green)
![DRF](https://img.shields.io/badge/DRF-3.15.2-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?style=flat&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=flat&logo=docker)
![black](https://img.shields.io/badge/black-24.8.0-black?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.75.0-009688.svg)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.17.0-ff69b4.svg)
![httpx](https://img.shields.io/badge/httpx-0.23.0-1EBEA5.svg)

 
## Описание проекта

Этот проект является тестовым заданием. 

### Часть 1. 

Проект предоставляет простой API для управления списком задач. Он построен с использованием Django и Django REST Framework, что позволяет  выполнять операции создания, чтения, обновления и удаления (CRUD) для задач.
В качестве БД используется PostgreSQL

## Функциональность

API предоставляет следующие возможности:

- **Получение списка задач** (GET)
- **Создание новой задачи** (POST)
- **Обновление существующей задачи** (PUT/PATCH)
- **Удаление задачи** (DELETE)

## Модель Task

Модель `Task` имеет следующие поля:

- `title`: Строка, длиной до 100 символов, обязательное поле.
- `description`: Текстовое поле, необязательное.
- `completed`: Булево значение, по умолчанию `False`.
Swagger доступен по адресу http://127.0.0.1:8001/swagger/


### Часть 2 

Это микросервис на **FastAPI**, который интегрируется с внешним REST API для получения информации о пользователях. Микросервис принимает запросы от клиента, отправляет их к внешнему API и возвращает данные обратно клиенту.

## Функции микросервиса

- Принимает запросы от клиента на получение информации о пользователе (id, имя, email).
- Отправляет запросы к внешнему API для получения данных о пользователе.
- Возвращает информацию о пользователе обратно клиенту.

порт: -8000 
## Установка и запуск

### Запуск


1. Клонируйте терепозиторий

    ```bash
    git clone https://github.com/yourusername/task-management-api.git
    cd task-management-api
2. Проверьте версию Docker и Docker Compose, либо установите:
    ```bash
    docker --version
    docker-compose --version
3. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build