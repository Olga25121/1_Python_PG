# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# x = int(input(' Введите число A: '))
# y = int(input(' Введите число B: '))

# def pow(a, n):
#     if (n == 1):
#         return a
#     else:
#         return a * pow(x, n - 1)
# print('->', pow(x, y))

     #2 Автотест
# a = 3
# b = 5

# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a
# print(f(a, b))



# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4

# def sum(A, B):
#     if (B==0):
#         return A
#     else:
#         return sum(A+1,B-1)

# a = int(input('Input A: '))
# print()
# b = int(input('Input B: '))
# print()
# if (a>=b):
#     print('->', sum(a,b))
# else:
#     print('->', sum(b,a))


     #2 Автотест

# a = 2
# b = 2

# def sum(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return sum(a + 1, b - 1)
    
# print(sum(a, b))
