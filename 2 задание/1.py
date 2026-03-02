input_line = input("Введите числа через пробел: ")
elements = input_line.split()

power = int(input("Введите степень: "))
result = []

for elem in elements:
    if elem.lstrip('-').isdigit():
        num = int(elem)           
        res = num ** power        
        result.append(res)
        
    else:
        res = elem * power        
        result.append(res)
        
print("Вывод:", *result)