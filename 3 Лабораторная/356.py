# В заданном списке, состоящем из целых чисел,
# найдите сумму и количество элементов списка, попавших в интервал [a; b].
# Для примера был взят список целых четных чисел
while True:
    try:
        a = int(input('Введите число, с которого начинается интервал: '))
        b = int(input('Введите число, которым заканчивается интервал: '))
        numbers = list(range(0, 10001, 2))         # Числа списка могут быть любые
        if numbers.index(a) >= numbers.index(b):   # Для примера целые положительные четные числа
            print('A по порядку должно стоять до числа B')
    except ValueError:
        print('A и B должны быть целыми числами пренадлежащими списку четных чисел от 0 до 10000')
    else:
        if numbers.index(a) < numbers.index(b):
            print(f'Cумма членов полученного списка равна: {sum(numbers[numbers.index(a):numbers.index(b)])}, '
                  f'а количество членов равно {len(numbers[numbers.index(a):numbers.index(b)])}')
    end = input("Чтобы повторить нажмите Enter, Чтобы закончить введите 1: ")
    if end == '1':
        break
