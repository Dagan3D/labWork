#IPv4 адрес - 4 цифры от 0 до 255 записаных через точку, в конце необходимо добавить '\n'
#мне кажется уже можно создавть класс под работу с ip :)

def listToIP (inIP: list) -> str:
    res = ""
    for i in range(3):
        res += str(inIP[i])+"."
    res += str(inIP[-1]) + "\n"
    return res

def IPToList(inList: str) -> list:    
    ip = list(map(int, inList.split('.')))
    if IPCorrect:
        return ip

def IPCorrect(inIP: list) -> bool:
    if len(inIP) != 4:
        return False
    for i in IP:
        if i < 0 and i > 255:
            return False
    return True

def requestIP() -> list: 
    try:
        while True:
            ip = IPToList(input("Введите маску: "))            
            for i in ip:
                if not IPCorrect:
                    raise ValueError
            break
    except ValueError:
        print("Ошибка ввода. Попробуйте ещё раз")
    return ip

def imposeMask (IP: list, mask: list) -> list:
    ip_solve = [0, 0, 0, 0]
    for i in range(4):
        ip_solve[i] = IP[i] & mask[i]
    return ip_solve

mask = requestIP()
res = ""

with open(".\ip.log", "r") as ip_file:
    IP = ip_file.readline()
    while IP:
        solve_ip = imposeMask(IPToList(IP), mask)
        IP = ip_file.readline()
        res += listToIP(solve_ip)

with open(".\ip_solve.log", "w") as ip_solve_file:
    ip_solve_file.write(res)