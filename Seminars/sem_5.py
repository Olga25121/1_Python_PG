# Сергей Сердюк через рекурсию найти факториал числа Х

# print('Введите число:')
# a = int(input())
# def Factorial(n):
#     if n == 0:
#         return 1
#     return n * Factorial(n - 1)
# print(Factorial(a))




# Задача №31. 
# Последовательностью Фибоначчи называется последовательность чисел 
# a0 , a1 , ..., an , ...,
# где a0 = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


      # Семинар
# def fib(n):
#     if n in [0, 1]:
#         return 1
#     return fib(n-1) + fib(n-2)
# n = int(input('Введите n: '))
# print(fib(n)) 

      #
    
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# num_list = []
# n = int(input())
# for i in range(1, n+1):
#     num_list.append(fib(i))
# print(num_list) 
# print(fib(n))    

    #

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
# n = int(input()) 
# print(fibonacci(n))


# Задача №33.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def change_marks(marks: list[int]) -> list[int]:
#     """Рекурсивная замена макисмальных оценок минимальными"""

#     max_mark = max(marks)
#     min_mark = min(marks)
#     marks[marks.index(max_mark)] = min_mark

#     if max_mark not in marks:
#         return marks
#     return change_marks(marks)


# print(change_marks([1, 2, 3, 1, 1, 3, 4, 4, 5, 4]))

# a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
# print(a.index(5))

# a[a.index(5)] = 1000
# print(a)



# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# 1 - не является простым числом

# Input: 5
# Output: yes 

      #Семинар

# x = int(input('Введите число: '))
# def simple_number(n, a = 2):
#     if n <= 1:
#         return False
#     if a * a > n:
#         return True
#     if n % a == 0:
#         return False
#     return simple_number(n, a + 1)
# if simple_number(x):
#     print('yes')
# else:
#     print('no')


     #Семинар
# def palindrom(n):
#     if len(n) <= 1:
#         return True
#     if n[0] == n[-1]:
#         return palindrom(n[1:-1])
#     return False
# a = str(input("Введите строку: "))
# if palindrom(a) == True:
#     print("Палиндром")
# else:
#     print("Не палиндром")

     #

# def isSimple(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n


# n = int(input())
# if isSimple(n):
#     print('YES')
# else:
#     print('NO')


# Задача №37. 
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

# arr = [1, 2, 3, 4, 5]
# print("Original array: ")
# for i in range(0, len(arr)):
#      print(arr[i])
# print("Array in reverse order: ")
# for i in range(len(arr)-1, -1, -1):
#      print(arr[i])

     # Seminar
# num = 3
# def Reverse(a):
#     if a == 0:
#         return '+'
#     print("Введите число: ")
#     number = input()
#     #return number + Reverse(a - 1) - тут введет в порядке, в котором вводили цифры
#     return Reverse(a - 1) + number

# print(Reverse(num))

