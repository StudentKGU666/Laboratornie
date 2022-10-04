# Дан список из 10 элементов.
# Первые 4 упорядочить по возрастанию, последние 4 по убыванию.
numbers = [12, 45, 6, 87, 1, 567, 41, 9, 76, 50]
first_section = numbers[0:4]
second_section = numbers[4:6]
third_section = numbers[6:10]
first_section.sort()
third_section.sort(reverse=True)
print(first_section + second_section + third_section)
# Короче не сделать, ругается на NoneType
