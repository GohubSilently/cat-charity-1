# Cat Charity - API сервис управления благотворительными проектами и пожертвованиями на базе фреймворка FastAPI.

[![Python](https://img.shields.io/badge/-Python-3771a1?style=flat&logo=Python&logoColor=ffffff)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=FastAPI&logoColor=ffffff)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-blue?style=flat&logo=sqlalchemy&logoColor=ffffff)](https://www.sqlalchemy.org/)  

Автор – [Халин Вадим](https://t.me/gohub1)

---

## Оглавление
- [Описание](#описание)  
- [Основные технологии](#основные-технологии)  
- [Запуск проекта](#запуск-проекта)

---

## Описание
Cat Charity — API сервис для управления благотворительными проектами и пожертвованиями.
Система позволяет:
- Создавать и редактировать проекты с указанной целью по сбору средств.  
- Вносить пожертвования в проекты.  
- Автоматически распределять пожертвования по незавершённым проектам (инвестирование).  
- Отслеживать статус проектов и пожертвований (полностью собранные/закрытые).  

Проект написан на FastAPI с асинхронной работой базы данных через SQLAlchemy.

---

## Основные технологии
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Alembic

---

## Запуск проекта
1. Клонируем репозиторий.
```
git clone git@github.com:GohubSilently/cat-charity-1.git && cd cat_charity
```

2. Установливаем зависимости.
```
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip && pip install -r requirements.tx
```

3. Настраиваем (.env).
```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
APP_DESCRIPTION=Сервис для поддержки котиков

DATABASE_URL=sqlite+aiosqlite:///./charity_fund.db
```

4. Запускаем миграции
```
alembic init
alembic upgrade head
```

5. Инициализируем проект.
```
uvicorn app.main:app --reload
```

6.  Документация будет доступна по этому адресу [API](http://127.0.0.1:8000/docs)

---
