import math

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

def pow_(a: float, b: float) -> float:
    return a ** b

def fact(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал только для целых неотрицательных чисел")
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def sqrt_(x: float) -> float:
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа")
    return math.sqrt(x)

def mod(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Остаток от деления на ноль")
    return a % b

ops = {
    "1": ("Сложение", add, 2),
    "2": ("Вычитание", sub, 2),
    "3": ("Умножение", mul, 2),
    "4": ("Деление", div, 2),
    "5": ("Степень", pow_, 2),
    "6": ("Факториал", fact, 1),
    "7": ("Корень", sqrt_, 1),
    "8": ("Остаток", mod, 2),
}

def show_menu():
    print("\nДоступные операции:")
    for key, (name, _, _) in ops.items():
        print(f"  {key}. {name}")
    print("  exit. Выход")

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")

# Основной цикл
while True:
    show_menu()
    choice = input("Выберите номер операции или exit: ").strip()
    if choice.lower() == "exit":
        print("Выход из калькулятора.")
        break
    if choice not in ops:
        print("Неверный номер")
        continue

    name, func, arity = ops[choice]
    try:
        if arity == 1:
            if name == "Факториал":
                x = get_int("Введите целое число: ")
                result = func(x)
            else:
                x = get_number("Введите число: ")
                result = func(x)
        else:
            x = get_number("Введите первое число: ")
            y = get_number("Введите второе число: ")
            result = func(x, y)
        print(">>>", result)
    except ValueError as e:
        print("Ошибка:", e)