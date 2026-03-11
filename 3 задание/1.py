from typing import List

def multiply(items: List[Union[int, float]], factor: float = 2) -> List[Union[int, float]]:
    result = []
    for x in items:
        result.append(x * factor)
    return result

def multiply_lambda(items: List[Union[int, float]], factor: float = 2) -> List[Union[int, float]]:
    return list(map(lambda x: x * factor, items))

input_str = input("Введите список чисел через пробел: ")
numbers = []
for part in input_str.split():
    try:
        if '.' in part:
            numbers.append(float(part))
        else:
            numbers.append(int(part))
    except ValueError:
        print(f"'{part}' не число, пропускаем")

mult = input("Введите множитель (по умолчанию 2): ")
if mult.strip() == "":
    factor = 2
else:
    factor = float(mult)

res1 = multiply(numbers, factor)
res2 = multiply_lambda(numbers, factor)

print("Результат (функция):", res1)
print("Результат (лямбда):", res2)
