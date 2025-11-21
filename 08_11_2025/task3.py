import tempfile
import os
import json

"""
TemporaryDirectory - временная директория для работы с временными файлами
"""

# Пример 1: Создание временных конфигов для бота
def setup_bot_environment(configs):
    """Создает временные конфигурационные файлы для бота"""
    
    # TODO: Создать временную директорию temp_dir
    with tempfile.TemporaryDirectory() as temp_dir:
        # TODO: Создать файл config.json с основными настройками
        with open(os.path.join(temp_dir, 'config.json'), 'w') as config_file:
            json.dump(configs, config_file)
        # TODO: Создать файл tokens.json с API токенами
        with open(os.path.join(temp_dir, 'tokens.json'), 'w') as tokens_file:
            json.dump(configs.get('main'), tokens_file)
        # TODO: Создать файл webhook.txt с URL вебхука
        with open(os.path.join(temp_dir, 'webhook.txt'), 'w') as webhook_file:
            webhook_file.write(configs.get('main').get('webhook'))
        # TODO: Вывести список созданных файлов в директории
        files = os.listdir(temp_dir)
        print(f"Cписок созданных файлов: {files}")

        print(f"Пример 1 - Временная директория: {temp_dir}")
        
    # Директория и все файлы автоматически удаляются

# Пример 2: Обработка временных медиа-файлов
def process_user_media(user_id, media_data):
    """Обрабатывает временные медиа-файлы пользователя"""
    
    # TODO: Создать временную директорию temp_dir
    with tempfile.TemporaryDirectory() as temp_dir:
        # TODO: Создать поддиректорию для пользователя
        user_dir = os.path.join(temp_dir, str(user_id))
        os.makedirs(user_dir)
        # TODO: Сохранить аватар пользователя в файл avatar.jpg
        with open(os.path.join(user_dir, 'avatar.jpg'), 'w') as media_file:
            media_file.write(media_data[0])
        # TODO: Сохранить дополнительные медиа в файлы media_1.jpg, media_2.jpg
        with open(os.path.join(user_dir, 'media_1.jpg'), 'w') as media_file:
            media_file.write(media_data[1])
        with open(os.path.join(user_dir, 'media_2.jpg'), 'w') as media_file:
            media_file.write(media_data[2])
        # TODO: Вывести информацию о созданных файлах
        files = os.listdir(user_dir)
        print(f"Cписок созданных файлов: {files}")
        
    print(f"Пример 2 - Обработка медиа для пользователя {user_id}")
        
    # Все медиа-файлы автоматически удаляются

# Пример 3: Временное кэширование данных бота
def cache_bot_data(cache_data):
    """Создает временный кэш данных бота"""
    
    # TODO: Создать временную директорию temp_dir
    with tempfile.TemporaryDirectory() as temp_dir:
        # TODO: Создать файл users_cache.json с кэшем пользователей
        users_cache_dir = os.path.join(temp_dir, 'users_cache.json')
        with open(users_cache_dir, 'w') as f:
            json.dump(cache_data.get('users'), f)
        # TODO: Создать файл messages_cache.json с кэшем сообщений
        messages_cache_dir = os.path.join(temp_dir, 'messages_cache.json')
        with open(messages_cache_dir, 'w') as f:
            json.dump(cache_data.get('messages'), f)
        # TODO: Создать файл state_cache.json с состоянием бота
        stats_cache_dir = os.path.join(temp_dir, 'stats_cache.json')
        with open(stats_cache_dir, 'w') as f:
            json.dump(cache_data, f)
        # TODO: Проверить существование созданных файлов
        if all([
            os.path.exists(users_cache_dir),
            os.path.exists(messages_cache_dir),
            os.path.exists(stats_cache_dir)
        ]):
            files = os.listdir(temp_dir)
            print(f"Cписок созданных файлов: {files}")
        else:
            raise FileNotFoundError("Файлы не найдены")
        
        print("Пример 3 - Кэширование данных бота")
        
    # Кэш автоматически очищается

# Пример 4: Создание временных логов
def create_temporary_logs(log_entries):
    """Создает временные лог-файлы для отладки"""
    
    # TODO: Создать временную директорию temp_dir
    with tempfile.TemporaryDirectory() as temp_dir:
        # TODO: Создать файл debug.log с отладочной информацией
        debug_dir = os.path.join(temp_dir, 'debug.log')
        with open(debug_dir, 'w') as f:
            f.write(log_entries[0])
        # TODO: Создать файл errors.log с ошибками
        errors_dir = os.path.join(temp_dir, 'errors.log')
        with open(errors_dir, 'w') as f:
            f.write(log_entries[1])
        # TODO: Создать файл actions.log с действиями пользователей
        actions_dir = os.path.join(temp_dir, 'actions.log')
        with open(actions_dir, 'w') as f:
            f.write(log_entries[2])
        # TODO: Посчитать общее количество записей в логах
        print(f"Общее количество записей в логах: {len(log_entries)}")

        print("Пример 4 - Временные логи для отладки")
        
    # Логи автоматически удаляются после отладки

# Демонстрация использования
if __name__ == "__main__":
    # Пример с конфигами бота
    bot_configs = {
        "main": {"token": "abc123", "webhook": "https://bot.com"},
        "database": {"host": "localhost", "port": 5432}
    }
    setup_bot_environment(bot_configs)
    
    # Пример с медиа-файлами
    media_data = ["avatar_data", "photo_1", "photo_2"]
    process_user_media(12345, media_data)
    
    # Пример с кэшированием
    cache_data = {
        "users": {"user1": "active", "user2": "inactive"},
        "messages": ["msg1", "msg2", "msg3"]
    }
    cache_bot_data(cache_data)
    
    # Пример с логами
    logs = [
        "DEBUG: Bot started",
        "ERROR: Connection failed", 
        "ACTION: User clicked button"
    ]
    create_temporary_logs(logs)