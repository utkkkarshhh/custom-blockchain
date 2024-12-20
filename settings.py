import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    class Secrets:
        SECRET_KEY = os.getenv("SECRET_KEY")
        DEBUG = os.getenv("DEBUG") == "True"
