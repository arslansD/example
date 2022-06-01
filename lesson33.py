# with open("lesson32.txt", "w", encoding="utf-8") as file:
#     for i in range(5):
#         name = input("введите имя: ")
#         grade = input("введите оценку: ")
#         file.write(f"{name} : {grade}\n")


# исходный код
# num1 = int(input("введите первое число: "))
# num2 = int(input("введите второе число: "))
# summary = num1 + num2
# print(summary)


# Базовый алгоритм проверки самого большого числа
# a = int(input("введите число 1: "))
# b = int(input("введите число 2: "))
# c = int(input("введите число 3: "))
# if a > b:
#     if a > c:
#         print(f"{a} самое большое число")
#     else:
#         print(f"{c} самое большое число")
# else:
#     if b > c:
#         print(f"{b} самое большое число")
#     else:
#         print(f"{c} самое большое число")






# x = 5
# y = 4
# print(x, y)
# x, y = y, x # как в питоне поменять местами элементы
# print(x, y)




# Пузырьковая сортировка в python
# def bubble_sort(nums):
#     swapped = True # заранее предполагаем, что список не отсортирован
#     while swapped:
#         swapped = False # цикл остановится, если список уже отсортирован
#         for i in range(len(nums)-1): # от начала до конца
#             if nums[i] > nums[i+1]: # сравниваем число слева с числом справа
#                 nums[i], nums[i+1] = nums[i+1], nums[i] # если слева больше, то меняем местами
#                 swapped = True # если число поменяли, то продолжаем цикл
# random_list = [6,4,2,2,6,5,2,1]
# bubble_sort(random_list)
# print(random_list)



# c = 10
# while c > 5: # проверка на условие, работает только в начале
#     c = 0
#     print("hey")



# #         0 1 2 3 4 5
# my_list = [1,2,3,4,5]
# length = len(my_list) # 5
# print(my_list[length-1])




# def selection_sort(nums):
#     for i in range(len(nums)): # i это количество уже отсортированных элементов
#         lowest_value_index = i # предположим, что первое число уже сортированно
#         for j in range(i+1, len(nums)): # пройдемся через все НЕ отсортированные чисел
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         # поменяем местами самое маленькое число, на первую свободную позицию
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
# random_list = [12,14,51,65,34,1,5,3]
# selection_sort(random_list)
# print(random_list)


# Пузырьковая сортировка - более эффективна, если список почти отсортирован
# Выборочная сортировка - МЕНЕЕ эффективна, если список почти отсортирован


# my_list = [9,5,4,6,3,1,4,6,2,1]
# print(sorted(my_list)) # создает новый отсортированный список и выводит его
# my_list.sort() # изменяет существующий список
# print(my_list)
# метод sort() быстрее, чем sorted()


# Добавить числа в список через list comprehension
# A = [1,2,3,4]
# X = 3
# B = [b for b in A if b < X] # list comprehension
# print(B)


# Обычный способ добавить числа в список
# A = [1,2,3,4]
# X = 3
# B = []
# for element in A:
#     if element < X:
#         B.append(element)
# print(B)
