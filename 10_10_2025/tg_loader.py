import os
import re
import pandas as pd
import json


class TextDataLoader():
    def __init__(self, file_path:str='data.json'):
        self.file_path = file_path
    
    def _validate_file_path(self):
        """Проверяет существование пути файла, что это файл (а не директория), расширение файла"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл '{self.file_path}' не существует")
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"'{self.file_path}' является директорией, а не файлом")
        if not self.file_path.endswith(".json"):
            raise ValueError(f"Ошибка расширения файла '{self.file_path}'")
    
    def load_data(self):
        """Загружает данные, при исключениях файловой системы выводит ошибку"""
        self._validate_file_path()
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            print("Данные успешно загружены")
            return json_data
        except json.decoder.JSONDecodeError:
            print(f"Ошибка декодирования файла '{self.file_path}'")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
    
    def extract_posts(self, json_data=None):
        """Извлекает текст и дату постов из датасета, генерирует id"""
        if json_data is None:
            json_data = self.load_data(self.file_path)
        posts = []
        # Проверяем наличие ключа 'messages' в данных
        if isinstance(json_data, dict) and 'messages' in json_data:
            messages = json_data['messages']
            # Обрабатываем каждый пост
            for message in messages:
                post_id = message.get('id')
                date = message.get('date')
                if isinstance(message, dict) and 'text' in message:
                    text = message['text']
                    # Обработка разных форматов текста
                    if isinstance(text, str) and text != '':
                        # Текст как строка
                        posts.append({'id': post_id, 'date': date, 'text': text})
                    elif isinstance(text, list):
                        # Текст как список элементов (разные форматы)
                        text_parts = []
                        for item in text:
                            if isinstance(item, str):
                                text_parts.append(item)
                            elif isinstance(item, dict) and 'text' in item:
                                text_parts.append(item['text'])
                        # Объединяем все части текста
                        if text_parts != '':
                            posts.append({'id': post_id, 'date': date, 'text': ''.join(text_parts)})
        return posts

    def clean_text(self, posts:list):
        """Очищает тексты из списка постов с помощью регулярных выражений"""
        if posts:
            for post in posts:
                text = str(post['text'])
                text = re.sub(r'[^\w\s.,!?-]', ' ', text)
                text = re.sub(r'[\s\n\t]+', ' ', text)
                text = text.lower().strip()
                post['text'] = text
        return posts

    def stats(self, posts:list):
        """Считает статистику по датасету: количество постов, длину в символах и токенах"""
        if posts:
            posts_num = len(posts)
            avg_sym_length = sum([len(post['text']) for post in posts]) / posts_num
            for post in posts:
                text_no_punc = re.sub(r'[^\w\s]', '', post['text'])
                avg_token_length = len(text_no_punc) / posts_num
                return posts_num, avg_sym_length, avg_token_length

    def save_to_csv(self, posts:list, output_path:str):
        """Сохраняет датасет в файл формата CSV"""
        df = pd.DataFrame(posts)
        df.to_csv(output_path, index=False)
        print(f"Данные сохранены в {output_path}")

# Пример применения класса
if __name__ == "__main__":
    # 1. Создание экземпляра
    text_loader = TextDataLoader("result.json")

    # 2. Загрузка данных
    json_data = text_loader.load_data()

    # 3. Извлечение постов
    posts = text_loader.extract_posts(json_data)

    # 4. Очистка текстов
    cleaned_posts = text_loader.clean_text(posts)

    # 5. Сохранение в CSV
    text_loader.save_to_csv(cleaned_posts, 'cleaned_posts.csv')

    # 6. Просмотр результатов
    print("\nПервые 3 очищенных поста:")
    for i, post in enumerate(cleaned_posts[:3]):
        print(f"{i + 1}) {post["text"][:100]}...")

    print(text_loader.stats(cleaned_posts))
