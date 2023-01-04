import re
s = input("Введите строку: /n")
x = input("Введите вирус:/n")
re.sub(x, "", s, flags=re.I)