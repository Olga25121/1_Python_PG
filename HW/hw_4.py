# Сергей Сердюк set1.intersection(set2)
# Сергей Сердюк set1 & set2

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input('Введите кол-во элементов первого множества: '))
# m = int(input('Введите кол-во элементов второго множества: '))
# n_elem = set(input('Введите сами элементы первого множества:').split())
# m_elem = set(input('Введите сами элементы второго множества:').split())
# print(n, m)
# print('--------------')
# print(n_elem)
# print(m_elem)
# print('--------------')
# res = n_elem.intersection(m_elem)
# print(*res)

     # 2 Автотест мой ответ

# var1 = '5 4' 
# var2 = '1 3 5 7 9'  # элементы первого множества через пробел
# var3 = '2 3 4 5' 

# # Введите ваше решение ниже
# set1 = set(map(int, var2.split()))   # Создаем множество из элементов первого множества
# set2 = set(map(int, var3.split()))
# num = sorted(list(set1 & set2))  # Находим пересечение множеств и сортируем числа
# res = ' '.join(map(str, num))          # Преобразуем числа в строки и объединяем их через пробел
# print(res)

     # Автотест Семинар
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
# v2 = set(var2.split())
# print(v2)
# v3 = set(var3.split())
# i = v2.intersection(v3)
# print(*sorted(i))

    # 3 Автотест
# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5' 

# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')

       # 4

# n = input('Введите сами элементы первого множества:').split()
# print(set(n))

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(set(n_set))
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(set(m_set))
# s_set = sorted(n_set.intersection(m_set))
# print('--------------')
# print(*s_set)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9


# from random import randint
# list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
# print(list_1)
# a = int(input('Введите № куста: '))
# res = 0
# if a == 1:
#     res = list_1[0] + list_1[1] + list_1[-1]
# elif a == len(list_1):
#     res = list_1[-2] + list_1[-1] + list_1[0]
# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
# print(res, 'ягод')




# berr = [5, 8, 6, 4, 9, 2, 7, 3]
# n = len(berr)

# # import random
# # n = int(input("Введите количество кустов: "))
# # berryes = list(random.randint(0, 10) for i in range(n))
# res = []
# i = 0
# sum = 0
# print(berr)

# while (i < n):
#     if (i == n - 1):
#         sum = berr[- 2] + berr[- 1] + berr[0]
#     else:
#         sum = berr[i] + berr[i - 1] + berr[i + 1]
#         res.append(sum)
#         res.sort()
#     i += 1

# print(f"Максимальное число ягод за один заход: {res[-1]}")


      # 2 Автотест
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# # Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))

























# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.


# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8