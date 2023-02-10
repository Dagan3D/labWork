import math


def hofstadter_f_m(n: int) -> list[int]:

    if type(n) != int:
        raise ValueError
    if n <= 0:
        raise ValueError

    num = 1
    F_res = [1]
    M_res = [0]
    while num < n:
        M = num - F_res[M_res[num - 1]]
        M_res.append(M)
        F = num - M_res[F_res[num - 1]]
        F_res.append(F)
        num += 1
        yield list(zip(F_res, M_res))


def main():
    while True:
        try:
            n: int = 0
            n = int(input("Введите колличество пар значений: "))
            a = hofstadter_f_m(n)
            for i in a:
                print(i)
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте снова")


if __name__ == "__main__":
    main()
