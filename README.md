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
```

4. Подготовка alembic env.py
```
import asyncio
import os
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context

from app.core.base import Base


load_dotenv()

config = context.config

config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
target_metadata = Base.metadata
```

5. Применение миграций
```
alembic revision --autogenerate -m "First migration"
alembic upgrade head
```

6. Файл .env
```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
APP_DESCRIPTION=Сервис для поддержки котиков

DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
```
