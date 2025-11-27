import math
import random
# Ввод количества слов
while True:
    try:
        n = int(input("Введите количество слов в тексте: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0")
    except ValueError:
        print("Введите целое число")
# Генерация текста
letters = 'йцукенгшщзхъфывапролджэячсмитьбюё'
words = []
for i in range(n):
    length = random.randint(3, 10)
    word = ''
    for x in range(length):
        word += random.choice(letters)
    words.append(word)
text = ' '.join(words)
print(f"Tекст: {text}")
# Анализ первых букв
letter_count = {}
for word in words:
    if word:
        first_letter = word[0].lower()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
# Поиск буквы с максимальным количеством слов
max_letter = ''
max_count = 0
for letter, count in letter_count.items():
    if count > max_count:
        max_letter = letter
        max_count = count
# Вывод результатов
print(f"Всего слов: {len(words)}")
print("Статистика:")

for letter in sorted(letter_count.keys()):
    print(f"'{letter}': {letter_count[letter]}")

print(f"Результат: больше всего слов начинается на букву '{max_letter}'")
print(f"Количество: {max_count}")
# print("Задача 2")
# while True:
#     text = input("Введите строку: ").strip()
#     if text:
#         break
#     print("Строка не может быть пустой!")
#
# print(f"Cтрока: {text}")
#
# latin = 0
# russian = 0
#
# try:
#
#     for char in text:
#         if char in '0123456789':
#             test = int("эта строка содержит цифры")
#
#         if 'a' <= char <= 'z':
#             latin += 1
#         elif 'а' <= char <= 'я':
#             russian += 1
#
#     # print(f"Латинских: {latin}")
#     # print(f"Русских: {russian}")
#     print(f"Общее количество букв: {latin + russian}")
#
# except ValueError:
#     print("В строке должны быть только буквы, попробуйте снова ")

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
# print("Задача 2")
# while True:
#     try:
#         x0 = float(input("Введите х0: "))
#         break
#     except ValueError:
#         print("Это не число. Попробуйте снова")
#
# while True:
#     try:
#         x1 = float(input("Введите х1: "))
#         break
#     except ValueError:
#         print("Это не число. Попробуйте снова")
#
# while True:
#     try:
#         dx = float(input("Введите dx: "))
#         break
#     except ValueError:
#         print("Это не число. Попробуйте снова")
#
# if x0 < x1 and dx > 0:
#     x = x0
#     while x < x1:
#         if x < 0:
#             z = x**2
#         elif 0 < x <= 1:
#             z = math.sin(x)
#         else:
#             z = math.cos(x)
#
#         x += dx
#         print("z =",z)
# elif x0 > x1 and dx < 0:
#     print(1)
# else:
#     print("ERROR")

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







