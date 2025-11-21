import tempfile
import json

"""
TemporaryFile - анонимный временный файл для безопасной работы с конфиденциальными данными
"""

# Пример 1: Безопасная работа с API ключами в боте
def process_sensitive_data(api_key, secret_token):
    """Обрабатывает конфиденциальные данные во временном файле"""
    
    with tempfile.TemporaryFile(mode='w+') as temp_file:
        # TODO: Создать словарь с учетными данными (api_key и secret_token)
        data_dict = {"api_key": api_key, "secret_token": secret_token}
        # TODO: Записать словарь в файл в формате JSON
        json.dump(data_dict, temp_file)
        # TODO: Вернуться в начало файла с помощью seek(0)
        temp_file.seek(0)
        # TODO: Прочитать данные и вывести первые 8 символов API ключа
        print(json.load(temp_file).get('api_key')[:8])

# Пример 2: Временное хранение токена авторизации
def handle_user_session(user_token):
    """Работа с токеном пользователя во временном файле"""
    
    with tempfile.TemporaryFile(mode='w+') as temp_file:
        # TODO: Записать user_token в файл
        temp_file.write(user_token)
        # TODO: Вернуться в начало файла с помощью seek(0)
        temp_file.seek(0)
        # TODO: Прочитать токен и вывести первые 10 символов
        print(temp_file.read(10))
        # TODO: Вернуться в начало и очистить файл с помощью truncate(0)
        temp_file.truncate(0)
        # TODO: Записать обновленный токен (старый + "_refreshed")
        temp_file.write(user_token + '_refreshed')

# Пример 3: Обработка временных конфигураций бота
def load_bot_configuration(config_data):
    """Загружает конфигурацию бота во временный файл"""
    
    with tempfile.TemporaryFile(mode='w+') as temp_file:
        # TODO: Записать config_data в файл в формате JSON с отступами=2
        json.dump(config_data, temp_file, indent=2)
        # TODO: Вернуться в начало файла с помощью seek(0)
        temp_file.seek(0)
        # TODO: Прочитать конфигурацию и вывести список ключей
        print(json.load(temp_file))

# Демонстрация использования
if __name__ == "__main__":
    # Пример с API ключами
    process_sensitive_data("sk-1234567890abcdef", "supersecrettoken123")
    
    # Пример с токеном пользователя
    handle_user_session("user_auth_token_xyz_987654")
    
    # Пример с конфигурацией бота
    bot_config = {
        "api_key": "telegram_bot_key",
        "webhook_url": "https://example.com/webhook",
        "admin_ids": [12345, 67890]
    }
    load_bot_configuration(bot_config)