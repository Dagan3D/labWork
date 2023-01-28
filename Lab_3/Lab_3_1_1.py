import math


def reducer(frac: tuple[int, int]) -> tuple[int, int]:
    NOD = math.gcd(frac[0], frac[1])
    return int(frac[0] / NOD), int(frac[1] / NOD)


def main():
    while True:
        try:
            a: int = 0
            b: int = 0
            a, b = map(int, input("Введите целочисленую дробь А/Б (А > Б): ").split('/'))
            if a >= b:
                raise ValueError
            fraction = reducer((a, b))
            print(f"{str(fraction[0])}/{str(fraction[1])}")
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте снова")


if __name__ == "__main__":
    main()
