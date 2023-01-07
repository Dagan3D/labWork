import re

s = input("Введите строку: ")
x = input("Введите вирус: ")
print(re.sub(x, "", s, flags=re.IGNORECASE))
