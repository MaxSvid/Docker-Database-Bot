# Configuration file with classes "settings" and "databaseSettings" for calls and connections 

# from config import settings

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    LEAD_ADMIN_USERNAME = os.getenv("LEAD_ADMIN_USERNAME")
    ADMIN_ID = os.getenv("ADMIN_ID")

settings = Settings()

class DatabaseSettings:
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_PORT_NUMBER = os.getenv("POSTGRES_PORT_NUMBER")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")


databaseSettings = DatabaseSettings()


