def append_to_file(text: str, filename: str):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

    # читаю файл и вывожу четные строки
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"\nСодержимое чётных строк файла {filename}:")
        for i, line in enumerate(lines):
            if i % 2 == 0:
                print(line.rstrip())


# (предварительно создам файл example.txt с несколькими строками)
# Сначала создам файл с начальными строками (для демонстрации)
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("Первая строка\nВторая строка\nТретья строка\nЧетвертая строка\n")

# Вызову функцию для добавления новой строки
append_to_file("Пятая строка", "example.txt")

# Проверю содержимое файла
print("\nФинальное содержимое файла example.txt:")
with open('example.txt', 'r', encoding='utf-8') as f:
    print(f.read())
