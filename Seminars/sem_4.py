# Введите цифры массива через пробел

# str = input().split() # Переводит цифры в список [...]
# print(str)

# Задача №25. 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# lst = input('a a a b c a a d c d d').split()
# k = 'a a a b c a a d c d d'
# lst = k.split()
# print(k)
# res = {}
# for i in lst:
#     if i not in res:
#         print(i, end=' ')
#         # res[i] = 1
#     else:
#         print(f'{i} _ {res[i]}', end=' ')
#         # res[i] += 1
#     res[i] = res.get(i, 0) + 1    #  если есть ключ метод GET возвращает res[i] = 1  or если нет ключа - res[i] += 1



# Задача №27. 
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13



# st ="She sells sea shells on the sea shore.\
# The shells that she sells are sea shells I'm sure.\
# So if she sells sea shells on the sea shore.\
# I'm sure that the shells are sea shore shells"
# print(st)
# st = st.lower()
# st = st.replace('.'," ")


# words = set (st.split(' '))
# print(words)
# print(len(words))




# Задача №29.
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:                          Петя:
# n = int(input())               n = int(input())
# max_number = 1000              max_number = -1
# while n != 0:                  while n < 0:
#  n = int(input())              n = int(input())
#  if max_number > n:            if max_number < n:
#  max_number = n           n = max_number
# print(max_number)              print(n)


# n = int(input('введи число N:'))
# if n!=0:
#     max_number = n
#     while n != 0:
#         if max_number < n:
#             max_number = n
#         n = int(input('введи следуещее число N:'))
#     print('максимальное число {}'.format(max_number))
# else:
#     print('чисел нет')


# Задача про холодильники

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


# ar = [ '222anton456, a1n1t1o1n1, 0000a0000n00t00000o000000n, gylfole, richard, ant0n']
# virus = 'anton'
# infected = []

#  for word in ar:
#   count = 0
# for char in word:
# if char == virus[count]:
# count += 1
# if count == len(virus):
# infected.append(word)
# count = 0


# import re
# for word in ar:
#     if re.search(r'a.*n.*t.*o.*n', word):
#         infected.append(word)
# print(' '.join(infected))


 
 
