def numberIsCorrect (inNum: str) -> int:
    num = int(inNum)
    if (num) < 0:
        raise ValueError
    return num

def one_step (inputList: list) -> list:
    res = inputList
    notNull = False
    for i, n in enumerate(res):
        if n != 0:
            res[i] -= 1
            notNull = True
        elif not notNull:
            pass
        else:
            return res
    return res

while True:
    try:    
        inputList = input("Введите целые положительные числа: ").split()
        inputList = list(map(numberIsCorrect, inputList))
        break

    except ValueError:
        print("Ошибка ввода. Попробуйте снова")

#print(inputList)
num = 0
while not all([i == 0 for i in inputList]):
    inputList = one_step(inputList)
    num += 1
    #print(inputList)
print(num)