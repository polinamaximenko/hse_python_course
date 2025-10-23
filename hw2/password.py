# Задача: Создать генератор паролей с настройками
# Использование:
#   python password.py --length 12
#   python password.py -l 16 --uppercase --digits --symbols
# Параметры: длина, uppercase, digits, symbols

import argparse
import string
import random


def generate_password(length: int = 8, uppercase=False, digits=False, symbols=False) -> str:
    """Генерирует пароль с учетом настроек"""

    # Проверка длины (больше нуля)
    if length <= 0:
        raise ValueError("Длина пароля должна быть положительным числом")

    # Базовый набор символов - строчные буквы
    characters = string.ascii_lowercase
    # Добавляем к набору доп. символы в зависимости от введенных параметров
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Проверка: длина пароля не меньше минимального требуемого набора символов
    required_categories = 1 + uppercase + digits + symbols
    if length < required_categories:
        raise ValueError(f"Для генерации пароля по заданным настройкам необходимо ввести длину от {required_categories} символов")

    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    parser = argparse.ArgumentParser(
        description='Генератор паролей с настройками',
        epilog='''
            Примеры использования:
              python password.py                                       # Пароль из 8 символов (только строчные буквы)
              python password.py --length 12 --digits                  # Пароль из 16 символов (строчные буквы и цифры)
              python password.py -l 16 --uppercase --digits --symbols  # Пароль из 16 символов (строчные и заглавные буквы, цифры, символы)
            '''
    )

    parser.add_argument('--length', '-l', type=int, default=8, help='Длина пароля (по умолчанию: 8)')

    parser.add_argument('--uppercase', '-u', action='store_true', help='Включать заглавные буквы')

    parser.add_argument('--digits', '-d', action='store_true', help='Включать цифры')

    parser.add_argument('--symbols', '-s', action='store_true', help='Включать специальные символы')

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        uppercase=args.uppercase,
        digits=args.digits,
        symbols=args.symbols
    )

    print(f"Сгенерированный пароль: {password}")


if __name__ == "__main__":
    main()


# Примеры применения:

# python password.py --length 12
# >>> Сгенерированный пароль: norpylbsyznx

# python password.py -l 16 --uppercase --digits --symbols
# >>> Сгенерированный пароль: ^|trtp<CYQux~Q)Z