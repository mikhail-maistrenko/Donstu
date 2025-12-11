import random
def create_matrix(n):
    return [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]
def print_matrix(A):
    for row in A:
        for elem in row:
            print(elem, end=' ')
        print()

def swap_diagonals(A):
    """Обработка главной диагонали - пример из теории стр. 3-4"""
    n = len(A)
    for i in range(n):
        # Обработка элементов главной диагонали (i == j)
        A[i][i], A[i][n - 1 - i] = A[i][n - 1 - i], A[i][i]
    return A


def task1():
    print("\n1. ПЕРЕСТАНОВКА ДИАГОНАЛЕЙ")

    # Ввод с проверкой
    n = 0
    while n <= 0:
        try:
            n = int(input("Размер матрицы N: "))
        except:
            print("Ошибка! Введите целое число.")

    # Создание матрицы
    A = create_matrix(n)

    print("\nИсходная матрица:")
    print_matrix(A)

    # Копирование матрицы (чтобы не менять исходную)
    B = []
    for i in range(n):  # Способ копирования из теории
        B.append(A[i][:])

    # Перестановка диагоналей
    swap_diagonals(B)

    print("\nПосле перестановки:")
    print_matrix(B)

print("Задание 2")
# Из файла: "Именные функции, инструкция def"
def DigitCountSum(K, C):
    """
    Функция из задания - пример функции с параметрами
    K - входной параметр
    C - будет содержать количество цифр (выходной параметр)
    Возвращает сумму цифр
    """
    count = 0
    sum_digits = 0
    num = K

    if num == 0:
        C = 1
        return 0, C

    while num > 0:
        sum_digits += num % 10
        count += 1
        num //= 10

    C = count  # Записываем в выходной параметр
    return sum_digits, C


def task2():
    print("\n2. ЦИФРЫ ЧИСЕЛ")

    numbers = []
    print("Введите 5 чисел:")

    for i in range(5):
        while True:
            try:
                num = int(input(f"Число {i + 1}: "))
                if num >= 0:
                    numbers.append(num)
                    break
                print("Число должно быть >= 0!")
            except:
                print("Ошибка ввода!")

    print("\nРезультат:")
    print("Число  | Цифр | Сумма цифр")
    # print("-" * 25)

    for num in numbers:
        C = 0  # Будет содержать количество цифр
        sum_d, C = DigitCountSum(num, C)
        print(f"{num:6} | {C:4} | {sum_d:10}")


# ====================== ЗАДАНИЕ 3 ======================
# Из файла: "Словари — основные методы и функции"
# def task3():
#     print("\n3. СЛОВАРЬ")
#
#     # Ввод количества
#     n = 0
#     while n <= 0:
#         try:
#             n = int(input("Количество слов в словаре: "))
#         except:
#             print("Ошибка! Введите целое число.")
#
#     # Создание словаря (пример из теории стр. 5)
#     dictionary = {}  # Пустой словарь
#
#     print(f"Введите {n} пар 'слово: определение':")
#     for i in range(n):
#         while True:
#             entry = input(f"{i + 1}: ")
#             if ':' in entry:
#
#
# rts = entry.split(':', 1)
# word = parts[0].strip()
# definition = parts[1].strip()
#
# if word and definition:
#     # Добавление элемента в словарь (пример стр. 7)
#     dictionary[word] = definition
#     break
# print("Формат: слово: определение")
#
# # Поиск в словаре (пример доступа стр. 6-7)
# print("\nПоиск (выход - 'выход'):")
# while True:
#     word = input("Слово: ").strip()
#     if word.lower() in ['выход', 'exit']:
#         break
#
#     # Используем метод get() из теории (стр. 7)
#     definition = dictionary.get(word)
#     if definition:
#         print(f"Определение: {definition}")
#     else:
#         print("Слово не найдено")
#

def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Перестановка диагоналей матрицы")
        print("2 - Подсчет цифр чисел")
        # print("3 - Словарь слов")
        # print("0 - Выход")

        choice = input("> ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        # elif choice == '3':
        #     task3()
        elif choice == '0':
            print("Выход.")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
