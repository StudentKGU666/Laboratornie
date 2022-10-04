# 3.49 Дано натуральное число n>=2, список списков, состоящий из n элементов по n чисел в элементе.
# Список заполняется случайным образом числами из промежутка от 0 до 199.
# Найти количество всех двухзначных чисел, у которых сумма цифр кратна 2.

from random import randint
while True:
    try:
        n = int(input('Введите целое число большее либо равное 2: '))
    except ValueError:
        print('Вы ввели либо не целое число, либо вообще не число')
    else:
        list_of_lists = []
        k = 0
        if n >= 2:
            while len(list_of_lists) != n:
                random_list = [randint(0, 199) for i in range(200)]
                list_of_lists.append(random_list[0:n])
                for i in range(len(random_list[0:n])):
                    for j in str(random_list[0:n][i]):
                        if random_list[0:n][i] in range(10, 100) and (int(j[0]) + int(j[-1])) % 2 == 0:
                            k += 1
            print(f'количество всех двухзначных чисел, у которых сумма цифр кратна 2 равно: {k}')
        if n < 2:
            print('Для числа n должно выполняться условие n >= 2')
    end = input("Чтобы повторить нажмите Enter, Чтобы закончить введите 1: ")
    if end == '1':
        break
