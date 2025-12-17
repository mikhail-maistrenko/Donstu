import random
def create_matrix(n):
    return [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]
def print_matrix(A):
    for row in A:
        for elem in row:
            print(elem, end=' ')
        print()

def swap_diagonals(A):
    n = len(A)
    for i in range(n):
        A[i][i], A[i][n - 1 - i] = A[i][n - 1 - i], A[i][i]
    return A


def task1():
    print("\n1. ПЕРЕСТАНОВКА ДИАГОНАЛЕЙ")

    n = 0
    while n <= 0:
        try:
            n = int(input("Размер матрицы N: "))
        except:
            print("Ошибка! Введите целое число")

    A = create_matrix(n)

    print("\nИсходная матрица:")
    print_matrix(A)


    B = []
    for i in range(n):
        B.append(A[i][:])


    swap_diagonals(B)

    print("\nПосле перестановки:")
    print_matrix(B)
########################
def DigitCountSum(K, C):

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

    C = count
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
                print("Число должно быть >= 0")
            except:
                print("Ошибка ввода!")

    print("\nРезультат:")
    print("Число  | Цифр | Сумма цифр")


    for num in numbers:
        C = 0
        sum_d, C = DigitCountSum(num, C)
        print(f"{num:6} | {C:4} | {sum_d:7}")

def task3():
    n = 0
    while n <= 0:
        try:
            n = int(input("Количество слов в словаре: "))
            dictionary = {}
            str = input()
            #слово: определение
            index = str.find(":")
            dictionary[str[:index]] = str[index + 1:]
        except:
            print("Ошибка! Введите целое число.")
    for i in range (n-1):
        line = input()
        index = line.find(":")
        dictionary=[line[:index]] = line[index + 1]
    search_word = input("Введите слово для поиска: ")

    if search_word in dictionary:
        print(f"Определение: {dictionary[search_word]}")
    else:
        print("Такого слова в словаре нет")

def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Перестановка диагоналей матрицы")
        print("2 - Подсчет цифр чисел")
        print("3 - Словарь слов")
        print("0 - Выход")

        choice = input("> ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '0':
            print("Выход")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()
