import os.path
from os import listdir

while True:
    try:
        min_size = int(input("Введите нижнюю границу: "))
        max_size = int(input("Введите верхнюю границу: "))
        break
    except ValueError:
        print("Ошибка ввода. Попробуйте снова")

files = listdir("./example")
n = 0
for file in files:
    if min_size < os.path.getsize("./example/" + file) < max_size:
        n += 1
print(n)
