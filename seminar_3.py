# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# n = int(input('Введите размер массива: '))
# numb = []
# for i in range(n):
#     numb.append(randint(0, 10))
# sum = 0
# for i in range(1, len(numb), 2):
#     sum += numb[i]
#     print(sum)

# print(f'Массив {numb}')
# print(f'Сумма нечетных элементов равна: {sum}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# from random import randint

# n = int(input('Введите размер списка: '))
# numb = []
# mult = []

# for i in range(n):
#     numb.append(randint(0, 10))

# for i in range(len(numb)):
#     while i < len(numb)/2 and n > len(numb)/2:
#         n = n-1
#         m = numb[i] * numb[n]
#         mult.append(m)
#         i+=1

# print(numb)
# print(mult)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# n = int(input('Введите размер списка: '))
# numb = []

# for i in range(n):
#     a = random.uniform(0, 10)
#     numb.append(round(a, 2))
    
# min = max = numb[0] % 1

# for i in range(len(numb)):
#     if numb[i] %1 < min:
#         min = numb[i] % 1
#     elif numb[i] %1 > max:
#         max = numb[i] % 1
#     else:
#         continue

# diff = round(max - min, 5)

# print(numb)
# print(diff)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))

# bin_d = bin(n)[2:]
# print(bin_d)

# a = ''

# while n > 0:
#     a = str(n % 2) + a
#     n = n // 2 
# print(a)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))

fibonacci = [0,1]
negative = [0,1]

for i in range(n-1):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

for i in range(n-1):
    negative.append(negative[-2] - negative[-1])

print(negative[::-1] + fibonacci[1:])