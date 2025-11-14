import requests
import tempfile
import json
import os
from time import time

def get_cached_weather_data(city: str, cache_minutes=10):
    """Получает данные о погоде с кэшированием во временный файл"""
    
    # TODO: Создать временный файл для получения пути к временной директории
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_filename = temp_file.name
        temp_dir = os.path.dirname(temp_filename)
        print(f"Файл создан: {temp_filename}")
    # TODO: Сформировать путь к кэш-файлу в формате "weather_город.json"
    # Пример:
    # cache_path = os.path.join(temp_dir, f"weather_{city}.json")
    # Пример создания пути: os.path.join('/tmp', 'file.txt') -> '/tmp/file.txt'
    cache_path = os.path.join(temp_dir, f"weather_{city}.json")
    
    # TODO: Проверить существование кэш-файла и его актуальность
    # Пример проверки существования файла: os.path.exists(cache_path)
    # Пример получения времени изменения: os.path.getmtime(cache_path)
    # Пример вычисления возраста файла: time() - os.path.getmtime(cache_path)
    # Если файл существует и его возраст меньше cache_minutes * 60 секунд:
    #   - вывести сообщение "Используем кэш для {city}"
    #   - прочитать и вернуть данные из файла
    if os.path.exists(cache_path) and (time() - os.path.getmtime(cache_path)) < cache_minutes * 60:
        print(f"Используем кэш для {city}")
        with open(cache_path, 'r') as cache_file:
            weather_data = json.load(cache_file)

    # TODO: Если кэша нет или он устарел - сделать запрос к API
    else:
        # Считываем API-ключ из файла
        with open("openweatherapi.txt", 'r', encoding='utf8') as f:
            appid = f.read().strip()
        try:
            # Запрос к API OpenWeatherMap
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            res_data = res.json()
            weather_data = {"city": city,
                            "conditions": res_data['weather'][0]['description'],
                            "temp": res_data['main']['temp'],
                            "feels_like": res_data['main']['feels_like'],
                            "temp_min": res_data['main']['temp_min'],
                            "temp_max": res_data['main']['temp_max'],
                            "pressure": res_data['main']['pressure'],
                            "wind_speed": res_data['wind']['speed']}

    # TODO: Сохранить полученные данные в кэш-файл
            with open(cache_path, 'w') as cache_file:
                json.dump(weather_data, cache_file)

        except Exception as e:
            print("Ошибка:", e)

    return weather_data

def cleanup_weather_cache():
    """Очищает все кэш-файлы погоды"""
    # TODO: Получить путь к временной директории через NamedTemporaryFile
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_filename = temp_file.name
        temp_dir = os.path.dirname(temp_filename)
    # TODO: Пройтись по всем файлам в директории
    # Пример получения списка файлов: os.listdir(temp_dir)
    # Пример проверки имени файла: 
    # file.startswith('weather_') and file.endswith('.json')
    # Пример удаления файла: os.unlink(os.path.join(temp_dir, file))
    # Пример полного пути: os.path.join(temp_dir, file)
    for file in os.listdir(temp_dir):
        if file.startswith('weather_') and file.endswith('.json'):
            os.unlink(os.path.join(temp_dir, file))
    print("Кэш очищен")

# Использование:
print(get_cached_weather_data("Moscow,RU"))
print(get_cached_weather_data("Moscow,RU"))  # Возьмет из кэша!
print(get_cached_weather_data("Saint Petersburg,RU"))

# В конце можно почистить
cleanup_weather_cache()