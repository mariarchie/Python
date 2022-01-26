# import random
# a = random.randint(2,23)
# print(a)

# 0. Вывести квадрат числа
# def f(x):
#     return x**2
# print(f(6))

# 1. По двум числам проверять, является ли первое квадратом второго
# def f(a, b):
#     return a == b**2
# print (f(9, -3))


# 2. Даны два числа. Показать большее и меньшее число
# def M(x1, x2):
#     return min(x1, x2), max(x1, x2) 
# print (M(34, 2))


# 3. По введенному номеру дня недели вывести его название
# WEEK = \
#     {
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wednesday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Saturday',
#         7: 'Sunday'
#     }
# A = int(input('Введите номер дня недели:'))
# print(WEEK[A])

# 5. Написать программу вычисления значения функции y = sin(x)/x
# from math import *
# def y(x):
#     return sin(x)/x
# print(y(28))

# 6. Выяснить является ли число чётным
# n=51
# print (n%2 == 0)

# 7. Показать числа от -N до N
# print ('Введите число N: ')
# n = int(input())
# for i in range(-n, n+1):
#    print (i)

# 9. Показать последнюю цифру трёхзначного числа
# print (n//10)%10

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# import random
# a = random.randint(10,99)
# print(a)
# def f(a):
#     s = a//10
#     f = a%10
#     if f > s:
#         return f
#     else:
#         return s
# print(f(a))

# 12. Удалить вторую цифру трехзначного числа
# def deleteSecond(abc):
#     c = abc%10
#     a = (abc//100)
#     ac = a*10 + c
#     return ac
# print (deleteSecond(409))

# 18 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# def logic(X, Y, Z):
#     return not (X or Y or Z) == (not X and not Y and not Z)
# for x in range (0,2):
#     for y in range (0,2):
#         for z in range (0,2):
#             print (logic(x, y, z))


# 19. Определить номер четверти плоскости, 
# в которой находится точка с координатами Х и У, 
# причем X ≠ 0 и Y ≠ 0
# x = 5
# y = 3
# if x > 0 and y > 0:
#     print ('первая четверть')
# elif x < 0 and y > 0:
#     print ('вторая четверть')
# elif x < 0 and y < 0:
#     print ('третья четверть')
# else:
#     print ('четвертая четверть')

# 20. Задать номер четверти, показать диапазоны для возможных координат
# QUARTER = \
#     {
#         1: 'X = (0;infinity); Y = (0;infinity)',
#         2: 'X = (-infinity;0); Y = (0;infinity)',
#         3: 'X = (-infinity;0); Y = (-infinity;0)',
#         4: 'X = (0;infinity); Y = (-infinity;0)',
#     }
# A = int(input('Введите номер дня четверти:'))
# print(QUARTER[A])

# 21. Программа проверяет пятизначное число на полиндром
# def Polin(r):
#     a = r % 10
#     b = (r%100)//10
#     d = (r//1000)%10
#     e = r//10000
#     return a==e and b==d
# print (Polin(92329))

# 22. Найти расстояние между точками в пространстве 2D/3D
# x1 = 5
# x2 = 8
# y1 = 10
# y2 = 15
# d = (x2-x1)**2 + (y2-y1)**2
# D = d**0.5
# print(D)


# 23. Показать таблицу квадратов чисел от 1 до N
# def D(N):
#     return [i**2 for i in range(1, N + 1)]
# print(D(5))


# 34. Написать программу замену элементов массива на противоположные
# mass1 = [1, 3, 5, 67, 34]
# i=0
# while i < len(mass1):
#     mass1[i]= -mass1[i]
#     i += 1
# print (mass1)



