# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];         - [2, 3, 5, 6] => [12, 15]

list_len = int(input('Введи длину списка = '))
list = [int(input(f'Введи {i} элемент списка -> ')) for i in range(list_len)]

#  !!!! Незнаю как правильно обрезать половину нечетного списка в сдку команду
#  по типу команды new_list[:], прошу подсказать.

new_list = []
if list_len % 2 == 0:
    for i in range(list_len // 2):
        new_list.append(list[i] * list[(-1) - i])
else:
    for i in range((list_len // 2) + 1):
        new_list.append(list[i] * list[(-1) - i])

print(list, '=>', new_list)