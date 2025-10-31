from tg_loader import TextDataLoader

"""
Создание своих функций проверок
"""

def assert_text_extracted(posts):
    """Кастомная функция проверки извлечения текста"""
    assert len(posts) == 2 and all(posts), "Должно быть 2 непустых поста"
    assert ("times new roman" not in posts[1]['text'] and
            "bold" not in posts[1]['text'] and
            "tag0" not in posts[0]['text']), "Должен извлекаться только текст поста"


def assert_text_cleaned(original_posts, cleaned_posts):
    """Кастомная функция проверки очистки текста"""
    for original, cleaned in zip(original_posts, cleaned_posts):
        assert cleaned["text"] == cleaned["text"].lower(), "Текст должен быть в нижнем регистре"
        assert cleaned["text"].strip() == cleaned["text"], "Не должно быть пробелов по краям"
        assert len(cleaned["text"].split()) <= len(original["text"].split()), "Не должно добавляться слов"
        assert (("#" not in cleaned["text"] and
                "@" not in cleaned["text"]), "Посты должны быть корректно очищены")


def test_with_custom_assertions():
    """Тест с кастомными проверками"""
    loader = TextDataLoader()

    # Подготовка данных
    json_data = {
        "messages": [
            {"text": "  FIRST POST  ", "tag": "tag0"},
            {"text": "Second @post! #hello #world", "font": "times new roman", "style": "bold"},
        ]
    }

    posts = loader.extract_posts(json_data)
    cleaned_posts = loader.clean_text(posts)

    assert_text_extracted(posts)
    assert_text_cleaned(posts, cleaned_posts)

test_with_custom_assertions()

"""
Перепишите тесты для методов clean_text и extract_posts используя:

- Assert с сообщениями об ошибках (2 любых теста)
- Множественные проверки в одном assert (2 любых теста)
- Создайте кастомную функцию, которая проверяет 2 теста сразу
"""