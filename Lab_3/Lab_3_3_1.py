from datetime import datetime as dt, timedelta


def nearest_date(*args: [str]) -> str:
    time_dif: list[timedelta] = []
    try:
        for date in args:
            date = dt.strptime(date, "%d.%m.%Y")
            #time_dif.append(dt(2023, 2, 10, 23, 0, 0) - date)
            time_dif.append(dt.now() - date)
    except ValueError:
        raise ValueError("Invalid date format")
    time_dif = sorted(enumerate(time_dif), key=lambda x: abs(x[1]))
    return args[time_dif[0][0]]


def main():
    #написано для даты 10.02.2023
    print(nearest_date("7.02.2023", "8.02.2023", "9.02.2023"))
    print(nearest_date("11.02.2023", "12.02.2023", "13.02.2023"))

    print(nearest_date("11.02.2023", "9.02.2023"))
    print(nearest_date("8.02.2023", "12.02.2023", "13.02.1923", "13.02.0223"))


if __name__ == "__main__":
    main()
