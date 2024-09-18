import math

def calc_one(num, op):
    match op:
        case "sin":
            return math.sin(num)
        case "cos":
            return math.cos(num)
        case "tg":
            return math.tan(num)
        case "ctg":
            return 1 / math.tan(num)
        case "ln":
            if num > 0 and num != 1:
                return math.log(num)
            return ValueError()


def calc_mult(first, second, op):
    match op:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            if second == 0:
                raise ValueError()
            return first / second


one_num_ops = ["sin", "cos", "tg", "ctg", "ln"]
mult_num_ops = ["+", "-", "/", "*"]

while True:
    first_num = input("Введите число: ")
    if not first_num.isdigit():
        print("Вы ввели не число")
        continue
    op = input("Введите операцию: ")
    if op in one_num_ops:
        try:
            print(calc_one(float(first_num), op))
        except:
            print("Функция не определена на этом значении")
    elif op in mult_num_ops:
        second_num = input("Введите число: ")
        if not second_num.isdigit():
            print("Вы ввели не число")
            continue

        try:
            print(calc_mult(float(first_num), float(second_num), op))
        except:
            print("Функция не определена на этом значении")
    else:
        print("Такой операции нет в списке")
