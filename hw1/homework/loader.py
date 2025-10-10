# Импорт класса
from loader_module import DataLoader

def dataloader_example(file_path):
    """Проверяет работу методов класса DataLoader()"""

    # 1. Создание экземпляра
    loader = DataLoader()

    # 2. Загрузка данных
    try:
        print(f"Загрузка данных из файла '{file_path}'...")
        data = loader.load_data(file_path)
        print("Данные успешно загружены!\n")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    # 3. Анализ данных
    try:
        info = loader.get_basic_info()
        print(info)
    except ValueError as e:
        print(f"Ошибка анализа: {e}")

    # 4. Работа с данными напрямую
    if loader.data is not None:
        print("\nПервые 5 строк данных:")
        print(loader.data.head())

# Вызов функции dataloader_example для 3 файлов-примеров
print("** Пример 1 **\n")
dataloader_example('health_metrics.csv')

print("\n** Пример 2 **\n")
dataloader_example('sales_data.csv')

print("\n** Пример 3 **\n")
dataloader_example('user_behavior.csv')
