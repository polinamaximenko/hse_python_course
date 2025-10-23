# Задача: Создать скрипт поиска файлов в папке по расширению
# Использование:
#   python finder.py /path/to/search --ext txt pdf
# Параметры: путь, расширения (nargs='+')

import argparse
import os

def find_files(search_path: str, extensions: list):
    """Находит файлы по расширениям в указанной директории"""

    # Проверяем существование пути
    if not os.path.exists(search_path):
        raise FileNotFoundError(f"Директория '{search_path}' не существует")
    # Проверяем, что это директория
    if not os.path.isdir(search_path):
        raise NotADirectoryError(f"'{search_path}' не является директорией")
    # Добавляем в список файлы с указанными расширениями
    found_files = []
    for f in os.listdir(search_path):
        cur_extension = os.path.splitext(f)[-1][1:]
        if cur_extension.lower() in extensions:
            found_files.append(f)
    if not found_files:
        print(f"Файлы с расширениями {extensions} не найдены в '{search_path}'")

    return sorted(found_files)


def main():
    parser = argparse.ArgumentParser(
        description='Поиск файлов по расширению в указанной директории',
        epilog='Пример использования: python finder.py /path/to/search --ext txt pdf'
    )

    parser.add_argument('search_path', type=str, help='Путь к директории для поиска')
    parser.add_argument('--ext', nargs='+', required=True, help='Расширения файлов для поиска (например: txt pdf docx)')

    args = parser.parse_args()

    found_files = find_files(
        search_path=args.search_path,
        extensions=args.ext,
    )
    if found_files:
        print(f"Найдено {len(found_files)} файлов:")
        print(*found_files, sep='\n')

if __name__ == "__main__":
    main()

# Примеры применения:

#   python finder.py \env_tests --ext py
# >>> Найдено 8 файлов:
#     1_type_annotation.py
#     2_argparse.py
#     calc.py
#     finder.py
#     password.py
#     tg_processor.py
#     todo.py
#     wordcount.py

#   python finder.py \env_tests --ext pdf docx
# >>> Файлы с расширениями ['pdf', 'docx'] не найдены в '\env_tests'