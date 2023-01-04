def numberIsCorrect (inNum: str) -> int:
    num = int(inNum)
    if (num) < 0:
        raise ValueError

while True:
    try:    
        inputList = input("Введите целые положительные числа: ").split()
        inputList = list(map(numberIsCorrect, inputList))
        break

    except ValueError:
        print("Ошибка ввода. Попробуйте снова")

 