# task.py

"""
Задание: 
1. Создать класс, который при инициализации читает JSON-файл и сохраняет 
   данные в атрибут data.
2. Реализовать метод get_song, который по id возвращает песню.
3. Реализовать метод find_similar, который по id песни возвращает список 
   похожих песен.

Условия:
1. Использовать api.json из этой папки
2. Написать не только модуль, но и пример его использования. 
3. При решении опираться на разобранные примеры.

Требования:
1. Создан класс с атрибутами для чтения файла
2. По умолчанию инициализируется имя файла "api.json"
3. Данные считываются с помощью инкапсулированного метода
4. Корректно произведено чтение JSON-файла 
5. В методе для чтения файла предсмотрена обработка ошибок "файл не найден"
   и "ошибка декодирования json" из библиотеки json (смотрим документацию)
6. Реализован поиск песни по ID (любым способом, но работает корректно)
7. Реализован поиск похожих песен (любым способом, но работает корректно)
8. Файл решения содержит образец использования (через __name__)
9. Все методы кроме __init__ содержат описания в Docstrings
10. Чистое, компактное решение
"""

class RecSys:
    def __init__(self, filename : str = 'api.json'):
        self.filename = filename
        self.data = self._read_file()
    
    def _read_file(self):
        """Читает данные из файла формата JSON"""
        import json
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
               return json.load(file)
        except FileNotFoundError:
             print(f"Ошибка: файл '{self.filename}' не найден")
        except json.JSONDecodeError:
             print(f"Ошибка декодирования JSON")      
        except Exception as e:
             print(f"Ошибка при чтении файла: {e}")
    
    def get_song(self, id : int):
        """Возвращает песню по её id"""
        try:
            for song in self.data:
                if song.get('id') == id:
                    return f"{song['performer']} - {song['title']}"
        except Exception as e:
             print(f"Ошибка при поиске песни: {e}")
    
    def find_similar(self, id : int):
        """Возвращает список похожих песен по id песни"""
        for song in self.data:
            try:
                if song.get('id') == id:
                    similar_songs = []
                    for i in song.get('similar_ids'):
                        similar_songs.append(self.get_song(i))
                    return similar_songs
            except Exception as e:
                print(f"Ошибка при поиске похожих песен: {e}")

if __name__ == '__main__':
    recsys = RecSys('api.json')
    print("Пример применения RecSys:")
    print(f"Поиск песни по индексу: {recsys.get_song(1)}")
    print(f"Поиск похожих песен: {recsys.find_similar(1)}")
