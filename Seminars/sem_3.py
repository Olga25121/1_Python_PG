# Задача №17. 
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# lst_1 = []
# for i in lst:
#     if i not in lst_1:
#         lst_1.append(i) # добавляет элемент справа строки
# print(len(lst_1))



# Задача №19. 
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# lst = [1, 2, 3, 4, 5]
# k = 4
# for i in range(k):
#     num = lst.pop()
#     lst.insert(0, num)   # вставка в 0 индекс -> сдвигает все элементы вправо
#     print(lst)



# Задача №21. 
# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

     # 1 Генератор цикла
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005 "},
# {"VII": "S005 "}, {"V": "S009"}, {"VIII": "S007"}]

# unq = set(value.strip() for item in data for value in item.values())
# print(unq)

#      # 2 Вложенные циклы
# dict_1 = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': ' S005 '},
# {'V': 'S009'}, {'VIII' : 'S007'}]
# print(dict_1)
# uniqe_set = set()
# for dictionary in dict_1:
#     for value in dictionary.values():
#         uniqe_set.add(value)
# print(uniqe_set)



# Задача №23. 
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)







       ###
# x = {"123": 123, (1, 1, 3) : "123", (1,2,3) : [1,2,3]}
# print(x)
# for i in x:
#     print(i)
# print(x[i])
# for i,j in x.items():
#     print(i,j)
# for i in x.values():
#     print(i)