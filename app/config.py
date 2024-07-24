from pydantic_settings import BaseSettings

class Cfg(BaseSettings):
    url: str = "localhost"
    port: int = 8080
    db: str = "sqlite:///./url.db"
    # mildly annoyed that pydantic uses config for this oh well
    class Config:
        env_file = ".env"


def get_config() -> Cfg:
    return Cfg()