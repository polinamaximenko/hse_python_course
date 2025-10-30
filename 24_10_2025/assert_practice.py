from tg_loader import TextDataLoader

def test_clean_text_with_assert():
    """Тестирование clean_text с использованием assert"""
    loader = TextDataLoader()
    
    # Тест очистки пробелов
    result = loader.clean_text([{"text": "  Hello  World  "}])
    assert result[0]['text'] == "hello world", "Должны удаляться лишние пробелы"
    
    # Тест нижнего регистра
    result = loader.clean_text([{"text": "HELLO"}])
    assert result[0]['text'] == "hello", "Текст должен быть в нижнем регистре"
    
    # Тест специальных символов
    result = loader.clean_text([{"text": "Hello! @user #tag"}])
    assert "#" not in result[0]['text'], "Должны удаляться # символы"
    assert "@" not in result[0]['text'], "Должны удаляться @ символы"
    
    # Тест знаков препинания
    result = loader.clean_text([{"text": "/=+$%`~"}])
    assert result[0]['text'] == "", "Должны удаляться знаки препинания"

    # Тест обработки пустых строк
    result = loader.clean_text([{"text": ""}])
    assert result[0]['text'] == "", "Пустые строки не должны обрабатываться"

    # Тест преобразования нестроковых данных
    result = loader.clean_text([{"text": 111}])
    assert isinstance(result[0]['text'], str), "Данные должны преобразовываться в строку"

test_clean_text_with_assert()

# 1. Замените импорт класса на ваш модуль
# 2. "Прогоните" тесты для вашего класса
# 3. Улучшите код при необходимости
# 4. Напишите еще один тест для проверки удаления хештегов и знаков препинания
# 5. Проверьте, что пустые строки никак не обрабатываются методом clean_text
# 6. Убедитесь в том, что нестроковые данные преобразовываются к виду строк 