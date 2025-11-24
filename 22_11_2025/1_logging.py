import requests
import logging
import os
import time
from typing import List, Dict, Optional

# Настройка логирования

# Задание 1: настройка логирования
# Устанавливаем минимальный уровень логирования - INFO
# Формат вывода: время - уровень - сообщение
# Создаем логгер с именем текущего модуля

### ваш код здесь ###
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    )

logger = logging.getLogger(__name__)

# Примеры использования разных уровней логирования:
# logger.debug("Отладочная информация")           # Не покажется (уровень INFO)
# logger.info("Информационное сообщение")         # Покажется - "2024-11-07 14:30:25 - INFO - Информационное сообщение"
# logger.warning("Предупреждение")                # Покажется - "2024-11-07 14:30:25 - WARNING - Предупреждение"
# logger.error("Сообщение об ошибке")             # Покажется - "2024-11-07 14:30:25 - ERROR - Сообщение об ошибке"
# logger.critical("Критическая ошибка")           # Покажется - "2024-11-07 14:30:25 - CRITICAL - Критическая ошибка"

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