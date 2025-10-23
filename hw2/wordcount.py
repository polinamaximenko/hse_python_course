# Задача: Создать скрипт для подсчета слов/символов в файле
# Использование:
#   python wordcount.py text.txt --words
#   python wordcount.py text.txt --chars --lines
# Опции: --words, --chars, --lines (можно комбинировать)

import argparse
import os

def wordcount(filepath: str, count_words=False, count_chars=False, count_lines=False) -> list:
    """Считает количество слов / символов / строк в текстовом файле"""

    # Проверка существования файла
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл '{filepath}' не существует")

    # Проверка: файл, а не директория
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"'{filepath}' является директорией, а не файлом")

    # Чтение файла
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

    # Подсчет статистики в зависимости от введенных параметров
    results = []
    if count_words:
        results.append(len(text.split()))
    if count_chars:
        results.append(len(text))
    if count_lines:
        results.append(len(text.splitlines()))
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Подсчитывает количество слов, символов и строк в текстовом файле',
        epilog='''
            Примеры использования:
            python wordcount.py text.txt --words            # Слова
            python wordcount.py text.txt --chars --lines    # Символы и строки
            python wordcount.py text.txt --words --chars    # Слова и символы
            '''
    )

    parser.add_argument('file', type=str, help='Путь к текстовому файлу')

    parser.add_argument('--words', action='store_true', help='Подсчитать количество слов в файле')

    parser.add_argument('--chars', action='store_true', help='Подсчитать количество символов в файле')

    parser.add_argument('--lines', action='store_true', help='Подсчитать количество строк в файле')

    args = parser.parse_args()

    print(*wordcount
        (
        filepath=args.file,
        count_words=args.words,
        count_chars=args.chars,
        count_lines=args.lines
    )
    )


if __name__ == "__main__":
    main()