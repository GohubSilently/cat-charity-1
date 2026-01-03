import uvicorn
from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(title=settings.app_title, description=settings.app_description)


if __name__ == "__main__":
    uvicorn.run(app, reload=True)
