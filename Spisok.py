import random
print("Задача 1")
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
print("Задача 3")
import random

# Ввод размера списка с проверкой
while True:
    try:
        n = int(input("Введите размер списка: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0!")
    except:
        print("Ошибка! Введите целое число.")

# Генерация случайного списка
numbers = []
for i in range(n):
    numbers.append(random.randint(-50, 50))

print(f"\nИсходный список: {numbers}")

# 1. Поиск максимального по модулю элемента
max_index = 0
max_abs = abs(numbers[0])

for i in range(1, len(numbers)):
    current_abs = abs(numbers[i])
    if current_abs > max_abs:
        max_abs = current_abs
        max_index = i

print(f"\n1. Максимальный по модулю элемент:")
print(f"   numbers[{max_index}] = {numbers[max_index]}")
print(f"   Модуль: {max_abs}")

# 2. Сумма после первого положительного
first_positive_index = -1
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive_index = i
        break

if first_positive_index == -1:
    print("\n2. В списке нет положительных элементов")
    sum_result = 0
else:
    sum_result = 0
    for i in range(first_positive_index + 1, len(numbers)):
        sum_result += numbers[i]

    print(f"\n2. Первый положительный элемент: numbers[{first_positive_index}] = {numbers[first_positive_index]}")
    print(f"   Сумма элементов после него: {sum_result}")

print(f"\nИтог: сумма = {sum_result}")