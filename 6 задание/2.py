def is_palindrome(s: str) -> bool:
    # Оставляем только буквы и цифры, приводим к нижнему регистру
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# Тесты
assert is_palindrome("Лёша на полке клопа нашёл") == True  # Сложный палиндром (из примера)
assert is_palindrome("А роза упала на лапу Азора") == True # Классика
assert is_palindrome("Python") == False                    # Не палиндром
assert is_palindrome("a") == True                         # Один символ
assert is_palindrome("") == True                          # Пустая строка (технически палиндром)
assert is_palindrome("1221") == True                      # Цифры

print("Функция палиндрома проверена.")