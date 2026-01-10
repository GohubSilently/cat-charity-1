1. Клонирование репозитория
```
git clone git@github.com:GohubSilently/cat-charity-1.git && cd cat-charity-1
```

2. Установка зависимостей (python 3.11)
```
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip && pip install -r requirements.tx
```

3. Запуск миграций
```
alembic init
alembic revision --autogenerate -m "Add charity and donation models"
alembic upgrade head
```

4. Файл .env
```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
APP_DESCRIPTION=Сервис для поддержки котиков

DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
```
