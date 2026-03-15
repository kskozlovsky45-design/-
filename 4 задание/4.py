def info_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция `{func.__name__}` вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper

@info_decorator
def calculate_area(length: float, width: float) -> float:
# Площадь прямоугольника
    return length * width

area = calculate_area(5, 10)
print(f"Площадь прямоугольника: {area}")

# С именованными аргументами:
area2 = calculate_area(length=7, width=3)
print(f"Площадь прямоугольника: {area2}")
