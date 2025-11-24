import requests
import logging
import os
import time
from typing import List, Dict, Optional
# Импортировать dotenv
from dotenv import load_dotenv

# Настройка логирования
### ваш код здесь ###
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    )
logger = logging.getLogger(__name__)

# Загрузить переменные окружения через dotenv
load_dotenv()

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
                        'description': item['snippet']['description'][:100] + '...' if item['snippet']['description'] else '',
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
