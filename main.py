import math
# print("Задача 1")
# while True:
#     try:
#         P = float(input("Введите Р процентов, 0 < P < 25: "))
#         if  0 < P < 25:
#             break
#         else:
#             print("Вы ошиблись, введенное Р процентов не соотвестует диапозону 0 < P < 25")
#     except ValueError:
#         print("Это не число. Попробуйте снова")
# S = 1000
# K = 0
# while S <= 1100:
#     S += S * (P / 100)
#     K += 1
# print("Количество месяцев К:",K)
# print("Итоговый размер вклада S:",S)
# ---------------------------------------------------------------
print("Задача 2")
while True:
    try:
        x0 = float(input("Введите х0: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова")

while True:
    try:
        x1 = float(input("Введите х1: "))
        if x1>x0:
            break
        else:
            print("x1 должен быть быть больше х0. Попробуйте снова")
    except ValueError:
        print("Это не число. Попробуйте снова")

while True:
    try:
        dx = float(input("Введите dx: "))
        if dx>0:
            break
        else:
            print("Шаг dx должен быть положительным.")
    except ValueError:
        print("Это не число. Попробуйте снова")

x = x0
while x < x1:
    if x < 0:
        z = x**2
    elif 0 < x <= 1:
        z = math.sin(x)
    else:
        z = math.cos(x)
    print("z = ",z)
    x += dx
 #-------------------------------------------------------------
# print("Задача 3")
# while True:
#     try:
#         N = int(input("Введите целое число N > 0: "))
#         if N > 0:
#             break
#         else:
#             print("Вы ошиблись, это число не соответствует условию N > 0")
#     except ValueError:
#         print("Вы ошиблись, это не целое число")
#
# last_del = 0
# while N > 0:
#     last_del = N % 10
#     print(last_del)
#     N //= 10