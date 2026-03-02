text = input("Введите строку: ")

words = text.split()

count_dict = {}

for word in words:
    low_word = word.lower()
    
    if low_word in count_dict:
        count_dict[low_word] += 1
        
    else:
        
        count_dict[low_word] = 1


for word, count in count_dict.items():
    print(f"{word}: {count}")