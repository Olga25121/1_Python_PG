# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# lst = []
# # n = int(input('Введите количество элементов в списке A: '))
# n = int(input())
# # print(n)
# for i in range(n):
#        lst.append(i + 1)
# print(*lst)              #Выводит список без квадратных скобок
# # x = int(input('Введите число X, которое необходимо найти в списке: '))
# x = int(input())
# # print(x)
# count = 0
# for i in range(n):
#        if lst[i] == x:
#               count += 1
# # print(f'Число {x} встречается в списке А {count} раз')
# print('->', count)

      # 2
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)

#       # 3
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for i in list_1:
#     if i == k:
#         count += 1
# print(count)

        # 4 Семинар count сам считает количество Х, цикл не нужен

# list_1 = [1, 1, 2, 3, 4, 5]
# print(list_1)
# x = int(input('Введите число X, которое необходимо найти в списке: '))
# num = list_1.count(x)
# print(num)



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# lst = []
# n = int(input())
# for i in range(n):
#     lst.append(i + 1)
# print(*lst)
# x = int(input())
# elem = abs(x - lst[0])
# index = 0
# for i in range(1, n):
#     count = abs(x - lst[i])
#     if count < elem:
#         elem = count
#         index = i
# print('->',lst[index])

      #2
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# # Введите ваше решение ниже

# elem = abs(k - list_1[0])
# index = 0
# for i in range(1, list_1[4]):
#     count = abs(k - list_1[i])
#     if count < elem:
#         elem = count
#         index = i
# print(list_1[index])


      #3
# N = abs(int(input('Введите количество элементов списка А: ')))
# A_entered = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     elem = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < elem:
#             elem = count
#             index = i
#     print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')


     # 4 Семинар  выводит две соседние цифры
# N = int(input('Введите количество элементов в массиве: '))
# lst_1 = list ()
# for i in range (N):
#     A = int(input('Введите значения массива: '))
#     lst_1.append(A)
# X = int(input('Введите значение X: '))
# lst_1 = [i for i in lst_1 if i != X]
# res = []
# elem = max(lst_1)
# for i in lst_1:
#     diff = abs(i - X)
#     if elem > diff:
#         elem = diff
#         res = [i]
#     elif elem == diff:
#         res.append(i)
# for i in res:
#     print(f'-> {i}')

        # 5 Автотест
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

       # 6 Автотест мое решение
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# res = []
# elem = max(list_1)
# for i in list_1:
#     i != k
#     diff = abs(i - k)
#     if elem > diff:
#         elem = diff
#         res = [i]
# for i in res:
#     print(i)


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12
# k = 'ноутбук'
# k = k.upper()
# # k = str.upper(input(k))
# print(k)
# scrabble = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ': 4, 'KЖЗХЦЧ': 5,
# 'JXШЭЮ': 8, 'QZФЩЪ': 10}
# sum = 0
# for i in k:
#     for key, value in scrabble.items():
#         if i in key:
#             sum = sum + value
# print(sum)

        # 2 Автотест

# k = 'ноутбук'

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
