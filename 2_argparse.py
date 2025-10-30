"""
СИНТАКСИС
"""

import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Описание программы',  # Описание в help
        epilog='Примеры использования'     # Текст в конце help
    )
    
    # Добавление аргументов...
    parser.add_argument('ключевое слово', help='Описание аргумента')
    
    args = parser.parse_args()  # Парсинг аргументов
    print(args)

if __name__ == "__main__":
    main()

"""
ПРИМЕР
"""

parser = argparse.ArgumentParser()

# Простой позиционный аргумент
parser.add_argument('filename', help='Имя файла для обработки')

# С указанием типа
parser.add_argument('count', type=int, help='Количество элементов')

args = parser.parse_args()
print(f"Обрабатываем файл: {args.filename}")
print(f"Количество: {args.count}")

"""
Как использовать?
"""

# python script.py data.txt 10

"""
Опциональные аргументы
"""

parser = argparse.ArgumentParser()

# Короткое и длинное имя
parser.add_argument('-v', '--verbose', help='Подробный вывод')

# Только длинное имя  
parser.add_argument('--output', help='Файл для сохранения')

# С действием (флаг)
parser.add_argument('--force', action='store_true', help='Принудительное выполнение')

args = parser.parse_args()

# python script.py --verbose --output result.txt
# python script.py -v --force

"""
Основные параметры
"""
parser.add_argument(
    '--input',                 # Имя аргумента
    type=str,                  # Тип данных
    default='data.json',       # Значение по умолчанию
    required=False,            # Обязательный аргумент
    help='Описание аргумента', # Помощь
    choices=['A', 'B', 'C'],   # Допустимые значения
    metavar='FILE',            # Имя в help
    nargs='+' # Заносит данные в список, причем если отсутствует хотя бы 1 аргумент, создаётся сообщение об ошибке
)

example.add_argument("--exception", "-e", type=str, default="", nargs='+', help="Исключить папки")

# Задача: Создать скрипт, который принимает два числа и операцию
# Использование: python calc.py 10 5 --operation add
# Должен поддерживать: add, subtract, multiply, divide

# Задача: Создать скрипт для подсчета слов/символов в файле
# Использование: 
#   python wordcount.py text.txt --words
#   python wordcount.py text.txt --chars --lines
# Опции: --words, --chars, --lines (можно комбинировать)

# Задача: Создать генератор паролей с настройками
# Использование:
#   python password.py --length 12
#   python password.py -l 16 --uppercase --digits --symbols
# Параметры: длина, uppercase, digits, symbols

# Задача: Создать скрипт поиска файлов в папке по расширению
# Использование:
#   python finder.py /path/to/search --ext txt pdf
# Параметры: путь, расширения (nargs='+')

# Задача: Создать менеджер задач с подкомандами
# Использование:
#   python todo.py add "Добавить интеграцию TG API"
#   python todo.py list --status pending
#   python todo.py complete 1
# Подкоманды: add, list, complete, delete