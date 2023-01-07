def numberIsCorrect (inNum: str) -> int:
    num = int(inNum)
    if (num) < 0:
        raise ValueError
    return num

book = dict()

while True:
    try:    
        m = int(input("Введите количество строк: "))
        break
    except ValueError:
        print("Ошибка ввода. Попробуйте снова")

for i in range(m):
    while True:
        try:    
            inputList = input("Введите место и цену билета: ").split()
            a, b, k = list(map(numberIsCorrect, inputList))
            if (a, b) in book:
                book[(a, b)].add(k)
            else:
                book[(a, b)] = {k}
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте снова")
    
for i in book:
    print(i[0], i[1],"-", len(book[i]))

pass
