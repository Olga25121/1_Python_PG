# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                             Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам            Парам пам-пам

         # 1
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# def rhythm(str):
#     str = str.split()
#     lst = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         lst.append(result)
#     return len(lst) == lst.count(lst[0])

# if len(stroka.split()) == 1:
#     print('Количество фраз должно быть больше одной!')
# else:
#     if rhythm(stroka):
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')


        # 2 Автотест
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#  print('Количество фраз должно быть больше одной!')
# else:
#  countVowels = []

#  for i in phrases:
#   countVowels.append(len([x for x in i if x.lower() in vowels]))

#  if countVowels.count(countVowels[0]) == len(countVowels):
#   print('Парам пам-пам')
#  else:
#   print('Пам парам')


           # 3 Семинар

# def gls_in_word(word):
#     vse_gls = "aeiouаеёиоуыэюя"
#     return sum(1 for char in word if char in vse_gls)

# def feel_the_rhythm(stroka):
#     stih = stroka.split()
#     if len(stih) <= 1:
#         return "Количество фраз должно быть больше одной!"

#     gls_in_stih = [gls_in_word(filter(str.isalpha, phrase)) for phrase in stih]    # str.isalpha - отсекает символы и цифры

#     if all(count == gls_in_stih[0] for count in gls_in_stih):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# stroka = 'пАра-ра-рАм рам-пам-папам па-ра-па-дам'
# print(feel_the_rhythm(stroka.lower()))




# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

         # 1

# def print_operation_table(operation, num_rows=9, num_columns=9,):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    
#     if num_columns > 2 and num_rows > 2:
#         for i in a:
#             print(*[f"{x:>1}" for x in i])
#     else:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
# print_operation_table(lambda x, y: x * y, 6, 6)


        # 2 Автотест

# def print_operation_table(operation, num_rows=9, num_columns=9): 
#     result = [] 
#     if num_rows < 2 or num_columns < 2: 
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
#     else: 
#         for i in range(1, num_rows + 1): 
#             for j in range(1, num_columns + 1): 
#                 if j != num_columns : 
#                     result.append(f'{operation(i, j)} ') 
#                 else: 
#                     result.append(operation(i, j)) 
#             result.append('\n') 
#         print(''.join([str(i) for i in result[:len(result) - 1]]))

        # 3 Семинар

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows<2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return  
#     res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]
#     for i in res:
#         print(*[f"{x} " for x in i])

# print_operation_table(lambda x, y: x * y, 3, 3)