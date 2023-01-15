from pydantic import BaseSettings


class Base(BaseSettings):
    TOKEN: str = 'SECRET'
    CHANNEL: str = 'SECRET'
    BOT_NAME: str = 'SECRET'
    WEBSOCKET: str = 'SECRET'


settings = Base()
