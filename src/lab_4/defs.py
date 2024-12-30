import io

# ----------------
# РАБОТА С ФАЙЛАМИ
# ----------------

def read_file(path):
    with io.open(path, "r", encoding='utf-8') as file:
        a = []
        line = file.readline()
        while line != "END":
            a.append(list(map(str, line.split(";"))))
            line = file.readline()
    file.close()
    return a

def write_file(path, output):
    with open(path, "w", encoding='UTF-8') as file:
        for i in output:
            file.write(f"{i}\n")

# ------------------
# ФУНКЦИИ ДЛЯ ЗАДАЧИ
# ------------------

# Проверка номера заказа
def check_id(id: str):
    if len(id) == 5 and id.isdigit():
        return True
    else:
        return False

# Получить корзину
def get_cart_dict(list1: str):
    list1 = list((list1.replace(" ","")).split(","))
    cart = dict()
    for i in range(0, len(list1)):
        if list1[i] not in cart:
            cart[list1[i]] = 1
        else:
            cart[list1[i]] += 1
    return cart

# Получить список продуктов (с учетом повторений)
def get_cart_list(cart: dict):
    line = ""
    cart_keys = list(cart.keys())
    # print(cart_keys)
    for i in range(0, len(cart_keys)):
        line += cart_keys[i]
        count = cart[cart_keys[i]]
        if count >= 2:
            line += " x" + str(count)
        line += ", "
    line = line[:-2]
    return line

# Проверка ФИО
def check_name(name: str):
    name = list(name.split(" "))
    if len(name) >= 2:
        return True
    else:
        return False

# Проверка адреса
def check_address(address: str):
    address = list((address.replace(" ","")).split("."))
    if len(address) == 4:
        return True
    else:
        return False

# Проверка номера телефона
def check_number(number: str):
    if len(number) != 16:
        return False
    elif number[0] != "+" or not (number[2] == number[6] == number[10] == number[13] == "-"):
        return False
    else:
        number = number[1:2] + number[3:6] + number[7:10] + number[11:13] + number[14:]
        return number.isdigit()

# Проверка приоритета доставки
def check_priority(priority: str):
    # print(priority)
    if priority not in ["LOW", "MIDDLE", "MAX"]:
        return False
    else:
        return True

# Получение сообщения о невалидном заказе
def error_message(a: list, error: int):
    line = a[0] + f";{error};"
    if error == 1:
        line += a[3]
    elif error == 2:
        line += a[4]
    else:
        line = f"{a[0]};1;{a[3]}\n{a[0]};2;{a[4]}"
    return line

# Замена пустых полей на "no data" и удаление "\n" из последнего аргумента заказа
def fix(a: list):
    for i in range(len(a)):
        if a[i] == "":
            a[i] = "no data"
    a[-1] = a[-1].replace("\n", "")
    return a

# Проверка всего заказа
def check_valid(a: list):
    ok = True
    error = 0
    # print(a)
    if not check_id(a[0]) or not check_name(a[2]) or not check_address(a[3]) or not check_number(a[4]) or not check_priority(str(a[5])):
        ok = False

        # СТАНДАРТНЫЕ ОШИБКИ

        if not check_address(a[3]):
            error = error + 1
            print(f"    Код ошибки 1. Ошибка в адресе: {a[3]}.")
        if not check_number(a[4]):
            error = error + 2
            print(f"    Код ошибки 2. Ошибка в номере телефона: {a[4]}.")

        # НЕСТАНДАРТНЫЕ ОШИБКИ

        if not check_id(a[0]):
            print(f"    Ошибка в номере заказа: {a[0]}.")
        if not check_name(a[2]):
            print(f"    Ошибка в ФИО: {a[2]}.")
        if not check_priority(a[5]):
            print(f"    Ошибка в приоритете доставки: {a[5]}.")
    else:
        print(f"    Ошибок не выявлено.")
    return ok, error