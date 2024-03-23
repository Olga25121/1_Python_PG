from turtle import clear



# Сложение строк

# print('Input the first num: ')
# a = input()
# b = input('Input the second num: ')
# print(a, "+", b, "=", a + b)


# Приведение типов:
# 1. Преобразование строки к целому числу  => int()

# a = 5.89
# print(a)
# print(type(a))  => float 5.89
# b = int(a)
# print(b)
# print(type(b))   => int  5

# 2. Преобразование любого типа данных в строку  => str()

# a = 5.89
# print(str(a))
# print(type(a))  => float  5.89
# a = str(a)
# print(str(a))
# print(type(a))  => str    5.89
# a = str(a)
# print(str(a) + '89')
# print(type(a))  => str    5.8989 

# 3. Преобразование любого типа данных в вещественный  => float()

# a = 2
# print(float(a))    2.0
# print(type(a))   => float  
# b = '5.89'
# print(float(b) * 2) 11.78
# print(type(b))   => float

# 4. Преобразование любого типа данных в логический  => bool()

# a = 1
# print(a)         1
# print(type(a))   => int
# a = bool(a)    
# print(a)         True
# print(type(a))   => bool


# Введение числа пользователем

# print('Input the first num: ')
# a = int(input())
# b = int(input('Input the second num: '))
# print(a, "+", b, "=", a + b)

# Округление числа

# a = 1.334654
# b = 5.677888
# print(round(a*b, 2))

# Управляющие конструкции: if, if-else

# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)

# Управляющие конструкции: else-if → в связке с elif (else if)

# username = input('Введите имя: ')
# if username == 'Mary':
#     print('Nice to see you, Mary!')
# elif username == 'Ilnar':
#     print('Ilnar is the best')
# else:
#     print('Hi, ', username)

# Логические операции and, or, not

# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')

# Управляющие конструкции: while 

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10         #3 
#     summa = summa + x
#     n = n // 10        #42
# print(summa)                # 9

# Управляющие конструкции: while-else

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# После выполнения данного кода в консоль выведется только цифра 3, то что
# находится внутри else будет игнорироваться, так как цикл завершился не
# самостоятельно.

# Пример программного кода без использования break:

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)

# Пожалуй
# хватит )
# 9


















