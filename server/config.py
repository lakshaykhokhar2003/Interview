import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

    @property
    def data_file_path(self) -> str:
        return os.getenv("DATA_FILE_PATH", "../assets/balance-sheet.json")  # Default value if not set

config = Config()