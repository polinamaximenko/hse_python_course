import requests
import logging
import os
import time
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    )

logger = logging.getLogger(__name__)
# Загрузка переменных окружения
load_dotenv()


class URLShortener:
    """
    Клиент для сервиса сокращения ссылок CleanURI

    Документация API: https://cleanuri.com/docs
    Не требует API ключа
    """

    def __init__(self):
        self.base_url = "https://cleanuri.com/api/v1/shorten"

    def shorten_url(self, long_url: str) -> Optional[str]:
        """Сокращает URL через cleanuri.com API"""
        try:
            response = requests.post(
                self.base_url,
                data={'url': long_url},
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                short_url = data.get('result_url')
                # logger.info выводит результат сокращения URL
                ### ваш код здесь ###
                logger.info(f"URL shortened: {self.base_url} -> {short_url}")
                # Пример вывода: "URL shortened: https://www.python.org/downloads/ -> https://cleanuri.com/xyz123"
                return short_url
            else:
                # logger.error выводит ошибку сокращения
                ### ваш код здесь ###
                logger.error(f"URL shortening error: {response.status_code}")
                # Пример вывода: "URL shortening error: 400 - Invalid URL"
                return None

        except requests.exceptions.RequestException as e:
            # logger.error выводит сетевую ошибку
            ### ваш код здесь ###
            logger.error(f"Network error during URL shortening: {e}")
            # Пример вывода: "Network error during URL shortening: Connection timed out"
            return None


class CryptoPriceChecker:
    """
    Клиент для получения цен криптовалют через CoinGecko API

    Документация: https://www.coingecko.com/api/documentations/v3
    Не требует API ключа для базовых запросов
    Список криптовалют: https://api.coingecko.com/api/v3/coins/list
    """

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_price(self, crypto_id: str) -> Optional[Dict]:
        """Получает текущую цену криптовалюты по ее ID"""
        try:
            params = {
                'ids': crypto_id,  # ID криптовалюты
                'vs_currencies': 'usd',  # Валюта для отображения цены
                'include_24hr_change': 'true'  # Включить изменение цены за 24 часа
            }

            ### ваш код здесь ###
            # Задание 2: сделать get-запрос
            # передать в запрос эндпоинт (base url),
            # параметры запроса (предыдущая строка этой функции)
            # и таймаут = 10
            response = requests.get(
                self.base_url,
                params=params,
                timeout=10
            )

            # Выполнить проверку кода запроса

            if response.status_code == 200:
                # Если 200:
                data = response.json()  # преобразует JSON ответ от API в Python словарь
                crypto_data = data.get(crypto_id)

                if crypto_data:
                    return {
                        'name': crypto_id.title(),
                        'current_price': crypto_data.get('usd'),
                        'price_change_24h': crypto_data.get('usd_24h_change'),
                        'currency': 'USD'
                    }
                else:
                    # logger.warning выводит предупреждение о ненайденной крипте
                    ### ваш код здесь ###
                    logger.warning(f"Cryptocurrency {crypto_id} not found")
                    # Пример вывода: "Cryptocurrency unknown_coin not found"
                    return None
            else:
                # logger.error выводит ошибку API
                ### ваш код здесь ###
                logger.error(f"CoinGecko API error: {response.status_code}")
                # Пример вывода: "CoinGecko API error: 429"
                return None

        except requests.exceptions.RequestException as e:
            # logger.error выводит сетевую ошибку
            ### ваш код здесь ###
            logger.error(f"Network error during price request: {e}")
            # Пример вывода: "Network error during price request: Connection refused"
            return None

    def get_multiple_prices(self, crypto_ids: List[str]) -> Dict[str, Optional[Dict]]:
        """Получает цены для нескольких криптовалют одновременно"""
        results = {}
        for crypto_id in crypto_ids:
            results[crypto_id] = self.get_price(crypto_id)
            # Задержка между запросами чтобы избежать лимитов API
            time.sleep(1)
        return results


class NewsAPIClient:
    """
    Клиент для получения новостей через NewsAPI

    Документация: https://newsapi.org/docs
    Получить API ключ: https://newsapi.org/register
    Бесплатный тариф: 100 запросов в день
    """

    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"

    def get_news(self, topic: str, max_results: int = 5) -> List[Dict]:
        """Получает новости по заданной теме"""
        if not self.api_key:
            # logger.error выводит ошибку отсутствия API ключа
            ### ваш код здесь ###
            logger.error("NEWS_API_KEY not found in .env file")
            # Пример вывода: "NEWS_API_KEY not found in .env file"
            # logger.info выводит подсказку где взять ключ
            ### ваш код здесь ###
            logger.error("Get free API key from: https://newsapi.org/register")
            # Пример вывода: "Get free API key from: https://newsapi.org/register"
            return []

        try:
            params = {
                'q': topic,
                'pageSize': min(max_results, 10),
                'apiKey': self.api_key,
                'language': 'en',
                'sortBy': 'publishedAt'
            }

            # Сделать get-запрос
            # Передать url, параметры и таймаут - 15
            # Проверить HTTP-ответы (на ошибки)
            ### ваш код здесь ###
            response = requests.get(
                self.base_url,
                params=params,
                timeout=15
            )

            # Если 200:
            if response.status_code == 200:
                # Получаем ответ как JSON
                data = response.json()
                articles = data.get('articles', [])

                news_list = []
                for article in articles[:max_results]:
                    news_list.append({
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'url': article.get('url', ''),
                        'published_at': article.get('publishedAt', ''),
                        'source': article.get('source', {}).get('name', '')
                    })

                # logger.info выводит количество найденных новостей
                ### ваш код здесь ###
                logger.info(f"Found {len(news_list)} news articles for topic '{topic}'")
                # Пример вывода: "Found 5 news articles for topic 'python programming'"
                return news_list

            elif response.status_code == 401:
                # logger.error выводит ошибку невалидного ключа
                ### ваш код здесь ###
                logger.error("Invalid NewsAPI key")
                # Пример вывода: "Invalid NewsAPI key"
                return []
            elif response.status_code == 429:
                # logger.warning выводит предупреждение о лимите запросов
                ### ваш код здесь ###
                logger.error("NewsAPI rate limit exceeded")
                # Пример вывода: "NewsAPI rate limit exceeded"
                return []
            else:
                # logger.error выводит ошибку API
                ### ваш код здесь ###
                logger.error(f"NewsAPI error: {response.status_code}")
                # Пример вывода: "NewsAPI error: 500"
                return []

        except requests.exceptions.RequestException as e:
            # logger.error выводит сетевую ошибку
            ### ваш код здесь ###
            logger.error(f"Network error during news request: {e}")
            # Пример вывода: "Network error during news request: Read timed out"
            return []


class IPGeolocation:
    """
    Клиент для определения геолокации по IP через ipapi.co

    Документация: https://ipapi.co/api/
    Не требует API ключа для базовых запросов
    Лимит: 1000 запросов в день
    """

    def __init__(self):
        self.base_url = "https://ipapi.co"

    def get_location(self, ip_address: str) -> Optional[Dict]:
        """Определяет геолокацию по IP адресу"""
        try:
            url = f"{self.base_url}/{ip_address}/json/"
            # Сделать get-запрос
            # Передать url и таймаут 10
            # Проверить HTTP-ответ, и если 200, то получить данные с API как JSON
            ### ваш код здесь ###
            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                # Проверяем есть ли ошибка в ответе
                if data.get('error'):
                    logger.error(f"Geolocation error: {data.get('reason')}")
                    return None

                return {
                    'ip': data.get('ip'),
                    'country': data.get('country_name'),
                    'city': data.get('city'),
                    'region': data.get('region'),
                    'timezone': data.get('timezone'),
                    'isp': data.get('org'),
                    'latitude': data.get('latitude'),
                    'longitude': data.get('longitude')
                }
            else:
                # logger.error выводит ошибку геолокации
                ### ваш код здесь ###
                logger.error(f"Geolocation error for IP {ip_address}: {response.status_code}")
                # Пример вывода: "Geolocation error for IP 999.999.999.999: 404"
                return None

        except requests.exceptions.RequestException as e:
            # logger.error(f"Network error during geolocation: {e}") выводит сетевую ошибку
            ### ваш код здесь ###
            logger.error(f"Network error during geolocation: {e}")
            # Пример вывода: "Network error during geolocation: Connection error"
            return None

    def get_own_ip_location(self) -> Optional[Dict]:
        """Определяет геолокацию собственного IP адреса"""
        try:
            # Сначала получаем свой внешний IP
            ip_response = requests.get('https://api.ipify.org', timeout=5)
            own_ip = ip_response.text.strip()
            # logger.info выводит обнаруженный IP
            ### ваш код здесь ###
            logger.info(f"Detected own IP: {own_ip}")
            # Пример вывода: "Detected own IP: 192.168.1.100"
            return self.get_location(own_ip)
        except requests.exceptions.RequestException as e:
            # logger.error выводит ошибку определения IP
            ### ваш код здесь ###
            logger.error(f"Error detecting own IP: {e}")
            # Пример вывода: "Error detecting own IP: Failed to resolve 'api.ipify.org'"
            return None


class YouTubeSearch:
    """
    Клиент для поиска видео через YouTube Data API

    Документация: https://developers.google.com/youtube/v3/docs/search/list
    Получить API ключ: https://console.cloud.google.com/apis/library/youtube.googleapis.com
    Бесплатный тариф: 10000 запросов в день
    """

    def __init__(self):
        self.api_key = os.getenv("YOUTUBE_API_KEY")
        self.base_url = "https://www.googleapis.com/youtube/v3/search"

    def search_videos(self, query: str, max_results: int = 5) -> List[Dict]:
        """Ищет видео на YouTube по запросу"""
        if not self.api_key:
            # logger.error выводит ошибку отсутствия API ключа
            ### ваш код здесь ###
            logger.error("YOUTUBE_API_KEY not found in .env file")
            # Пример вывода: "YOUTUBE_API_KEY not found in .env file"
            # logger.info выводит подсказку где взять ключ
            ### ваш код здесь ###
            logger.error("Get API key from: https://console.cloud.google.com/apis/library/youtube.googleapis.com")
            # Пример вывода: "Get API key from: https://console.cloud.google.com/apis/library/youtube.googleapis.com"
            return []

        try:
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': min(max_results, 10),
                'key': self.api_key
            }

            # Сделать get-запрос
            # Передать url, параметры, таймаут 15
            response = requests.get(self.base_url, params=params, timeout=15)
            # Проверить HTTP-ответ
            # Если код 200, получить json
            # Создать пустой список videos
            ### ваш код здесь ###
            if response.status_code == 200:
                data = response.json()
                videos = []

                for item in data.get('items', []):
                    video_data = {
                        'title': item['snippet']['title'],
                        'video_id': item['id']['videoId'],
                        'channel_title': item['snippet']['channelTitle'],
                        'published_at': item['snippet']['publishedAt'],
                        'description': item['snippet']['description'][:100] + '...' if item['snippet'][
                            'description'] else '',
                        'url': f"https://youtube.com/watch?v={item['id']['videoId']}"
                    }
                    videos.append(video_data)

                # logger.info выводит количество найденных видео
                ### ваш код здесь ###
                logger.info(f"Found {len(videos)} videos for query '{query}'")
                # Пример вывода: "Found 5 videos for query 'python tutorials'"
                return videos

            elif response.status_code == 403:
                # logger.error выводит ошибку аутентификации или квоты
                ### ваш код здесь ###
                logger.error("YouTube API authentication error or quota exceeded")
                # Пример вывода: "YouTube API authentication error or quota exceeded"
                return []
            else:
                # logger.error выводит ошибку API
                ### ваш код здесь ###
                logger.error(f"YouTube API error: {response.status_code}")
                # Пример вывода: "YouTube API error: 400"
                return []

        except requests.exceptions.RequestException as e:
            # logger.error выводит сетевую ошибку
            ### ваш код здесь ###
            logger.error(f"Network error during video search: {e}")
            # Пример вывода: "Network error during video search: SSL certificate verify failed"
            return []


# Демонстрация работы всех клиентов
if __name__ == "__main__":

    # logger.info выводит заголовок теста
    ### ваш код здесь ###
    logger.info("Testing URL Shortener...")
    # Пример вывода: "Testing URL Shortener..."
    shortener = URLShortener()
    short_url = shortener.shorten_url("https://www.python.org/downloads/")
    if short_url:
        # logger.info выводит сокращенную ссылку
        ### ваш код здесь ###
        logger.info(f"Short URL: {short_url}")
        # Пример вывода: "Short URL: https://cleanuri.com/xyz123"


    # logger.info выводит заголовок теста
    ### ваш код здесь ###
    logger.info("Testing Cryptocurrency Prices...")
    # Пример вывода: "Testing Cryptocurrency Prices..."
    crypto = CryptoPriceChecker()

    # Тестируем несколько криптовалют
    cryptocurrencies = ['bitcoin', 'ethereum', 'cardano', 'solana', 'dogecoin']
    prices = crypto.get_multiple_prices(cryptocurrencies)

    for crypto_id, price_data in prices.items():
        if price_data:
            change = price_data['price_change_24h'] or 0
            change_symbol = "+" if change > 0 else ""
            # logger.info выводит цену крипты с изменением
            ### ваш код здесь ###
            logger.info(f"{crypto_id}: ${price_data["current_price"]} ({change_symbol}{change:.2f}%)")
            # Пример вывода: "bitcoin: $45000.50 (+2.35%)"


    # logger.info выводит заголовок теста
    ### ваш код здесь ###
    logger.info("Testing News API...")
    # Пример вывода: "Testing News API..."
    news = NewsAPIClient()
    if news.api_key:
        python_news = news.get_news("python programming", max_results=3)
        for i, article in enumerate(python_news):
            # logger.info выводит заголовок новости
            ### ваш код здесь ###
            logger.info(f"Article {i+1}: {article["title"]}")
            # Пример вывода: "News: Python 3.11 Released with Major Performance Improvements"
    else:
        # logger.warning выводит предупреждение о ненастроенном ключе
        ### ваш код здесь ###
        logger.warning("NewsAPI key not configured")
        # Пример вывода: "NewsAPI key not configured"


    # logger.info выводит заголовок теста
    ### ваш код здесь ###
    logger.info("Testing IP Geolocation...")
    # Пример вывода: "Testing IP Geolocation..."
    geo = IPGeolocation()

    # Тестируем несколько IP адресов
    test_ips = ['8.8.8.8', '1.1.1.1', '23.94.48.109']
    for ip in test_ips:
        location = geo.get_location(ip)
        if location:
            # logger.info выводит информацию о геолокации
            ### ваш код здесь ###
            logger.info(f"IP {ip}: {location}")
            # Пример вывода: "IP 8.8.8.8: Mountain View, United States (Google LLC)"

    # Определяем свою геолокацию
    own_location = geo.get_own_ip_location()
    if own_location:
        # logger.info выводит местоположение пользователя
        ### ваш код здесь ###
        logger.info(f"Your location: {own_location}")
        # Пример вывода: "Your location: Moscow, Russia"


    # logger.info выводит заголовок теста
    ### ваш код здесь ###
    logger.info("Testing YouTube Search...")
    # Пример вывода: "Testing YouTube Search..."
    youtube = YouTubeSearch()
    if youtube.api_key:
        videos = youtube.search_videos("python tutorials", max_results=3)
        for i, video in enumerate(videos):
            # logger.info выводит название видео
            ### ваш код здесь ###
            logger.info(f"{i+1}. '{video['title']}' by {video['channel_title']}")
            # Пример вывода: "YouTube: Python Tutorial for Beginners - Learn Python in 1 Hour"
    else:
        # logger.warning выводит предупреждение о ненастроенном ключе
        ### ваш код здесь ###
        logger.warning("YouTube API key not configured")
        # Пример вывода: "YouTube API key not configured"
