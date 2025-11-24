import requests
import logging, os
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

class SimpleWebsiteChecker:
    """
    ЗАДАНИЕ: Реализуйте класс для проверки доступности сайтов
    
    ТРЕБОВАНИЯ:
    1. Метод check_website должен принимать URL и возвращать boolean
    2. Использовать requests.get с timeout=5
    3. Логировать успешные и неуспешные проверки
    4. Обрабатывать исключения requests.exceptions.RequestException
    """
    
    def check_website(self, url: str) -> bool:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logger.info(f"Сайт {url} доступен")
                return True
            else:
                logger.warning(f"Сайт {url} вернул статус {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при проверке сайта {url}: {e}")
            return False


class SimpleGitHubClient:
    """
    ЗАДАНИЕ: Реализуйте клиент для GitHub API
    
    ТРЕБОВАНИЯ:
    1. Метод get_user_info должен возвращать информацию о пользователе
    2. Использовать базовый URL: https://api.github.com
    3. Обрабатывать статус коды (200 - успех, 404 - пользователь не найден)
    4. Возвращать словарь с ключами: name, public_repos, followers
    5. Логировать ошибки и предупреждения
    """
    
    def __init__(self):
        self.base_url = "https://api.github.com"
    
    def get_user_info(self, username: str) -> Optional[Dict]:
        url = f"{self.base_url}/users/{username}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                data_dict = {"name": data.get("name"),
                             "public_repos": data.get("public_repos"),
                             "followers": data.get("followers")}
                return data_dict
            elif response.status_code == 404:
                logger.error(f"Пользователь {username} не найден")
            else:
                logger.error(f"Код статуса: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе: {e}")


class SimpleWeatherClient:
    """
    ЗАДАНИЕ: Реализуйте клиент для OpenWeatherMap API
    
    ТРЕБОВАНИЯ:
    1. API ключ должен браться из переменной окружения OPENWEATHER_API_KEY
    2. Базовый URL: https://api.openweathermap.org/data/2.5/weather
    3. Параметры запроса: q (город), appid (API ключ), units (metric)
    4. Возвращать словарь с: city, temperature, description
    5. Обрабатывать случаи когда API ключ не настроен
    """
    
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str) -> Optional[Dict]:
        if not self.api_key:
            logger.error("API ключ не настроен")

        params = {"q": city, "appid": self.api_key, "units": "metric"}

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                data_dict = {"city": data["name"],
                             "temperature": data["main"]["temp"],
                             "description": data["weather"][0]["description"]}
                return data_dict
            else:
                logger.error(f"Код статуса: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе: {e}")

class SimpleGoogleSearch:
    """
    ЗАДАНИЕ: Реализуйте клиент для Google Custom Search API
    
    ТРЕБОВАНИЯ:
    1. API ключ и Search Engine ID из переменных окружения
    2. Базовый URL: https://www.googleapis.com/customsearch/v1
    3. Параметры: key, cx, q, num (ограничить максимум 10 результатов)
    4. Возвращать список словарей с: title, url, snippet
    5. Обрабатывать ошибки API и случаи когда ключи не настроены
    """
    
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        self.base_url = "https://www.googleapis.com/customsearch/v1"
    
    def search(self, query: str, num_results: int = 5) -> List[Dict]:
        if not self.api_key:
            logger.error("API ключ не настроен")
        if not self.search_engine_id:
            logger.error("Search Engine ID не настроен")

        if num_results > 10:
            num_results = 10

        params = {"key": self.api_key,
                  "cx": self.search_engine_id,
                  "q": query,
                  "num": num_results}

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                results = []
                for item in data.get("items", []):
                    data_dict = {"title": item.get("title"),
                                 "url": item.get("link"),
                                 "snippet": item.get("snippet")}
                    results.append(data_dict)
                return results
            else:
                logger.error(f"Код статуса: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе: {e}")
            return []

# Пример использования
if __name__ == "__main__":
    # Проверка сайта
    checker = SimpleWebsiteChecker()
    result = checker.check_website("https://example.com")
    print(result)
    
    # GitHub
    github = SimpleGitHubClient()
    user_info = github.get_user_info("torvalds")
    print(user_info)
    
    # Погода
    weather = SimpleWeatherClient()
    weather_data = weather.get_weather("London")
    print(weather_data)
    
    # Поиск в Google
    google = SimpleGoogleSearch()
    search_results = google.search("python programming")
    print(search_results)
    
