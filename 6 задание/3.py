import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):

    def test_zero(self):
        # Факториал 0 всегда 1
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        # Обычное положительное число
        self.assertEqual(factorial(5), 120)

    def test_one(self):
        # Факториал 1
        self.assertEqual(factorial(1), 1)

    def test_negative_error(self):
        # Проверка вызова исключения для отрицательных чисел
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_large_value_error(self):
        # Проверка ограничения по sys.maxsize (например, очень большое число)
        with self.assertRaises(ValueError):
            factorial(10 ** 5)

if __name__ == "__main__":
    unittest.main()