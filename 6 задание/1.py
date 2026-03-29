def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

# Тесты
assert average_num([1, 1]) == 1.0                # Целые числа
assert average_num([2.5, 3.5]) == 3.0            # Числа с плавающей точкой
assert average_num([1, 2, 3]) == 2.0             # Несколько целых
assert average_num([-1, 1]) == 0.0               # Отрицательные числа
assert average_num([10, 20, 35]) == 21.67        # Проверка округления до 2 знаков
assert average_num(["5", 5]) == 5.0              # Конвертация строки в число
assert average_num([100]) == 100.0               # Один элемент
assert average_num(["1.5", 2]) == "Bad request"  # Ошибка конвертации (int() не берет "1.5")
assert average_num(["abc", 1]) == "Bad request"  # Явно некорректная строка
assert average_num([None, 1]) == "Bad request"   # Некорректный тип данных

print("Все assert тесты пройдены.")