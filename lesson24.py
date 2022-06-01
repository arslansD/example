# from lesson23 import students # Импортировали из другого файла, функцию
# students(name = "Farrad", grade = 123)
# students(name = "Vika", grade = 1236)
# students(name = "Orhan", grade = 878)





# def multiply(n):
#     count = 0
#     for elem in str(n):
#         if elem.isdigit(): # проверка, является ли элемент числом
#             count += 1 # если это число, то к длине +1
#     result = n * 5 ** len(str(n))
#             # -123 умножаем на позитивное число
#     print(result)
# multiply(-123)




# Дано 10 уникальных целых чисел.
# Среди них выведите самое большое число
# и его позицию.

# 4 3 5 # пример чисел
# 1 2 3 # как мы смотрим (позиция)
# 0 1 2 # как смотрит компьютер (индекс)



# my_list = []
# for elem in range(10): # принимаем 10 чисел
#     my_list.append(int(input("введите число: ")))
#
# max_n = max(my_list) # узнаем макс число через команду
# index_n = my_list.index(max_n) + 1 # узнаем позицию
# print(my_list) # выводим список
# print(max_n, index_n) # выводим число и позицию


# my_list = input("введите числа: ").split() # Принимаем элементы через пробел
# my_list = list(map(int, my_list)) # превращаем их в числа
# print(max(my_list), my_list.index(max(my_list))+1) # узнаем макс число, и позицию

# Напишите программу, которая считывает два целых числа X и Y.
# Выведите все числа между X и Y,
# которые при делении на 5 дают остаток равный 2 или 3.
# Если таких чисел не нашлось выведите “No any number”.
# 11 - 18 -> 12, 13, 17, 18
# x = int(input("введите число: "))
# y = int(input("введите число: "))
# check = 0
# if y > x:
#     num2, num1 = y, x
# else:
#     num2, num1 = x, y
#
# for elem in range(num1, num2+1):
#     if elem % 5 == 2 or elem % 5 == 3:
#         print(elem)
#         check = 1
# if check == 0:
#     print("Таких чисел нет")



# Задача с codeforces
# num = int(input("сколько чисел: "))
# my_list = list(map(int, input().split()))
# if my_list[0] % 2 == 0:
#     check = 2
# else:
#     check = 1
#
# for element in my_list:
#     if check == 2:
#         if element % 2 != 0:
#             print(my_list.index(element)+1)
#     else:
#         if element % 2 == 0:
#             print(my_list.index(element)+1)












