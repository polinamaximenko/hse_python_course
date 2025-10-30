def add(number1, number2):
    return number1 + number2


def multiply(number1, number2):
    return number1 * number2

if __name__ == '__main__':
    n1, n2 = 3, 5
    print(f"Сумма чисел: {add(n1, n2)}")
    print(f"Произведение чисел: {multiply(n1, n2)}")