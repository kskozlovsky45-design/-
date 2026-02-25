UInput = input("Введите число: ")

# Проверяем, состоит ли строка только из цифр (это значит, что число положительное и целое)
if UInput.isdigit():
    number = int(UInput)  # преобразуем в число
    if number % 2 == 0:
        print(f"Число {number} - четное")
    else:
        print(f"Число {number} - нечетное")
else:
    print("Ошибка: введено не число")