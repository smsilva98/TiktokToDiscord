from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    username: str
    webdriver_port: str | int = 4444
    windows: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
