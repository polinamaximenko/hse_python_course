from tg_loader import TextDataLoader

def test_extract_posts_comprehensive():
    """Комплексное тестирование extract_posts с assert"""
    loader = TextDataLoader()
    
    # Тестовые данные
    sample_data = {
        "name": "Test",
        "messages": [
            {"id": 1, "text": "Post 1", "other_field": "value"},
            {"id": 2, "text": "Post 2"}
        ]
    }
    
    result = loader.extract_posts(sample_data)
    
    # Проверки: допишите код для тестирования метода extract_posts
    assert isinstance(result, list), "Результат должен быть списком"
    assert len(result) == 2, "Должно быть извлечено 2 поста"
    assert result[0]["text"] == "Post 1", "Первый пост должен быть 'Post 1'"
    assert result[1]["text"] == "Post 2", "Второй пост должен быть 'Post 2'"
    assert all(isinstance(post["text"], str) for post in result), "Все элементы должны быть строками"

test_extract_posts_comprehensive()

# Пустой вывод: все тесты пройдены