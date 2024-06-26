# Task 1. Ввести два числа и определить большее из них.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print(f'{a} больше чем {b}')
elif a == b:
    print(f'{a} равно {b}')
else:
    print(f'{b} больше чем {a}')

### 1.1 Определить вес продукта.

a = int(input("Введите вес: "))

if a < 50:
    print(f's')
elif a < 80:       # 50 < a < 80
    print(f'm')
else:
    print(f'x')

# Task 2. За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
n=int(input("Введите расстояние за день: "))
m=int(input("Введите требуемое расстояние маршрута: "))
# print(f'Весь маршрут займет {(n + m - 1) // n} дня/день')
###
a = abs(-m//n)     # модуль числа 
print(f'Весь маршрут займет {a} дня/день')


# Task 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22 (ввод чисел НЕ в одну строку)
# Output: 32

cl1 = 20
cl2 = 21
cl3 = 22

sum = cl1 + cl2 + cl3
desk1 = abs(-cl1 // 2)
desk2 = (cl2 + 1) // 2
desk3 = cl3 // 2 + (cl3 % 2 != 0)
desk = desk1 + desk2 + desk3
print("desks needed: ")
print(desk)


# Task 5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
# В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# Input: 3 4 (ввод на разных строках)
# Output: 6




# Task 7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# Input: 2016
# Output: YES


