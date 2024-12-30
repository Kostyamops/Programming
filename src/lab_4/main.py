from defs import *


def main():
    valid = []
    non_valid = []
    for order in read_file("../../txtf/lab_4/input/all_errors.txt"):
        order = fix(order)
        print(f"Заказ номер {order[0]}:")
        ok, error = check_valid(order)
        if ok:
            # Обновление формата корзины
            order[1] = get_cart_list(get_cart_dict(order[1]))

            # Обновление формата адреса
            new_adress = list((order[3]).split("."))
            order.append(new_adress[0])
            order[3] = f"{new_adress[1][1:]}.{new_adress[2]}.{new_adress[3]}"

            # Добавление номера приоритета
            if order[5] == "LOW":
                order.append(0)
            elif order[5] == "MIDDLE":
                order.append(1)
            else:
                order.append(2)

            # Добавление в список валидных заказов
            valid.append(order)
        else:
            # Добавление в список невалидных заказов
            non_valid.append(error_message(order, error))

    # print(*valid, sep="\n")
    # print(*non_valid, sep="\n")

    valid.sort(key=lambda order: (order[-2], -order[-1]))

    # print(*valid, sep="\n")

    russian_orders = []
    other_orders = []
    for i in range(0, len(valid)):
        # print(i)
        if valid[i][-2] == "Россия":
            russian_orders.append(valid[i])
        else:
            other_orders.append(valid[i])

    # print(*russian_orders, sep="\n")
    # print(*other_orders, sep="\n")

    valid = []
    for i in russian_orders:
        valid.append(f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]}")
    for i in other_orders:
        valid.append(f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]}")

    # print(*valid, sep="\n")
    # print(*non_valid, sep="\n")

    write_file("../../txtf/lab_4/output/order_country.txt", valid)
    write_file("../../txtf/lab_4/output/non_valid_orders.txt", non_valid)

if __name__ == "__main__":
    main()