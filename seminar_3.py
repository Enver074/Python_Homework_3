# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = int(input('Введите размер массива: '))
numb = []
for i in range(n):
    numb.append(randint(0, 10))
sum = 0
for i in range(1, len(numb), 2):
    sum += numb[i]
    print(sum)

print(f'Массив {numb}')
print(f'Сумма нечетных элементов равна: {sum}')
