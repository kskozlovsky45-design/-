line1 = input("Введите первый список: ")
list1 = list(map(int, line1.split()))

line2 = input("Введите второй список: ")
list2 = list(map(int, line2.split()))

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

print("Общие элементы:", *common)