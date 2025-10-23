# Задача: Создать скрипт, который принимает два числа и операцию
# Использование: python calc.py 10 5 --operation add
# Должен поддерживать: add, subtract, multiply, divide

import argparse
from typing import Union

def calc(x: Union[int, float], y: Union[int, float], operation: str):
    """Применяет одну из 4 базовых мат. операций к двум числам"""

    # Проверка формата чисел
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Неверно введены числа")
    # Сложение
    if operation == 'add':
        return x + y
    # Вычитание
    elif operation == "subtract":
        return x - y
    # Умножение
    elif operation == "multiply":
        return x * y
    # Деление (с проверкой делителя)
    elif operation == "divide":
        if y == 0:
            return ZeroDivisionError("Деление на 0 невозможно!")
        else:
            return x / y
    
def main():
    parser = argparse.ArgumentParser(
        description='Калькулятор для базовых операций с двумя числами',
        epilog='''
            Примеры использования: 
            python calc.py 10 5 --operation add        # Сложение
            python calc.py 10 5 --operation subtract   # Вычитание
            python calc.py 10 5 --operation multiply   # Умножение
            python calc.py 10 5 --operation divide     # Деление
            '''
    )
    parser.add_argument('x', type=float, help='Число 1')
    parser.add_argument('y', type=float, help='Число 2')
    parser.add_argument('--operation',
                        type=str,
                        choices=["add", "subtract", "multiply", "divide"], 
                        help='Математическая операция')
        
    args = parser.parse_args()
    print(calc(args.x, args.y, args.operation))

if __name__ == "__main__":
    main()

# Примеры применения:

# python calc.py 10 5 --operation add
# >>> 15.0

# python calc.py 10 5 --operation subtract
# >>> 5.0

# python calc.py 10 5 --operation multiply
# >>> 50.0

# python calc.py 10 0 --operation divide
# >>> Деление на 0 невозможно!
