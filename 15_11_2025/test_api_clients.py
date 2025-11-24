import os
from dotenv import load_dotenv

load_dotenv()

def test_environment():
    """Проверка что переменные окружения загружены"""
    assert os.getenv("OPENWEATHER_API_KEY"), "OPENWEATHER_API_KEY not set"
    assert os.getenv("GOOGLE_SEARCH_API_KEY"), "GOOGLE_SEARCH_API_KEY not set"
    assert os.getenv("GOOGLE_SEARCH_ENGINE_ID"), "GOOGLE_SEARCH_ENGINE_ID not set"
    print("Environment variables loaded successfully")

if __name__ == "__main__":
    test_environment()