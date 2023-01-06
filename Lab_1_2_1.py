def numberIsCorrect (inNum: str) -> int:
    num = int(inNum)
    if (num) < 0:
        raise ValueError
    return num

def one_step (inputList: list) -> list:
    res = inputList
    for i, n in enumerate(res):
        if n != 0:
            res[i] -= 1
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

inputList = one_step(inputList)
print(inputList)
inputList = one_step(inputList)
print(inputList)
inputList = one_step(inputList)
print(inputList)
inputList = one_step(inputList)
print(inputList)
inputList = one_step(inputList)
print(inputList)