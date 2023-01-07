#IPv4 адрес - 4 цифры от 0 до 255 записаных через точку, в конце необходимо добавить \n

def listToIP (IP: list) -> str:
    res = ""
    for i in range(3):
        res += str(IP[i])+"."
    res += str(IP[-1]) + "\n"
    return res

def plus1 (ip: list, i: int):
    if ip[i] < 255:
        ip[i] += 1
    else:
        ip[i] = 0
        plus1(ip, i-1)

def string_formating(numberOfIP: int) -> str:
    res = ""
    ip = [192, 168, 0, 0]
    n = 0
    i = 3
    while n < numberOfIP:
        plus1(ip, i)
        n += 1
        res += listToIP(ip)
    return res

with open(".\ip.log", "w") as ip_file:
    ip_file.write(string_formating(10000))