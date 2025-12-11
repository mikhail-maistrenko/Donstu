import random
print("Задача 1")
while True:
    try:
        n = int(input("Введите количество слов в тексте: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0")
    except ValueError:
        print("Введите целое число")

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

letter_count = {}
for word in words:
    if word:
        first_letter = word[0].lower()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1

max_letter = ''
max_count = 0
for letter, count in letter_count.items():
    if count > max_count:
        max_letter = letter
        max_count = count

print(f"Всего слов: {len(words)}")

for letter in sorted(letter_count.keys()):
    print(f"'{letter}': {letter_count[letter]}")

print(f"Больше всего слов начинается на букву '{max_letter}'")
print(f"Количество: {max_count}")
#################################
print("Задача 2")
while True:
    text = input("Введите строку: ").strip()
    if text:
        break
    print("Строка не может быть пустой!")


print(f"Cтрока: {text}")

latin = 0
russian = 0
try:
    for x in text:
        if x in '0123456789':
            test = int("Эта строка содержит цифры")

        if 'a' <= x <= 'z':
            latin += 1
        elif 'а' <= x <= 'я':
            russian += 1

    print(f"Kоличество букв: {latin + russian}")
except ValueError:
    print("В строке должны быть только буквы, попробуйте снова ")
##############################################################
print("Задача 3")
while True:
    try:
        n = int(input("Введите размер списка: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше нуля")
    except:
        print("Введите целое число.")

numbers = []
for i in range(n):
    numbers.append(random.randint(-100, 100))
print(f"Исходный список: {numbers}")

max_index = 0
max_abs = abs(numbers[0])

for i in range(1, len(numbers)):
    temporary_abs = abs(numbers[i])
    if temporary_abs > max_abs:
        max_abs = temporary_abs
        max_index = i

print(f"1) Максимальный по модулю элемент:")
print(f"numbers[{max_index}] = {numbers[max_index]}")
print(f"Модуль: {max_abs}")

first_plus_index = -1
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_plus_index = i
        break

if first_plus_index == -1:
    print("2) В списке нет положительных элементов")
    sum_result = 0
else:
    sum_result = 0
    for i in range(first_plus_index + 1, len(numbers)):
        sum_result += numbers[i]
    print(f"2) Первый положительный элемент: numbers[{first_plus_index}] = {numbers[first_plus_index]}")
    print(f"Сумма элементов после него: {sum_result}")


