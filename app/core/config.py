from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд'
    app_description: str = 'Сервис для поддержки котиков'

    database_url: str = 'sqlite+aiosqlite:///./charity_fund.db'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
