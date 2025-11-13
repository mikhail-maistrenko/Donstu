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
# # ---------------------------------------------------------------
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
        break
    except ValueError:
        print("Это не число. Попробуйте снова")

while True:
    try:
        dx = float(input("Введите dx: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова")

if x0 < x1 and dx > 0:
    x = x0
    while x < x1:
        if x < 0:
            z = x**2
        elif 0 < x <= 1:
            z = math.sin(x)
        else:
            z = math.cos(x)

        x += dx
        print("z =",z)
elif x0 > x1 and dx < 0:
    print(1)
else:
    print("ERROR")
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
#         print("Вы ошиблись, это не число")
#
# delenie = 0
# while N > 0:
#     delenie = N % 10
#     N = N // 10
#     print(delenie)







