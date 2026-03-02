dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keyset = set(dct)
valueset = set(dct.values())

print("Множество ключей:", keyset)
print("Множество значений:", valueset)

unionset = keyset | valueset

print("Объединение множеств:", unionset)