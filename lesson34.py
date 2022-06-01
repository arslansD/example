# my_list = ["Orhan", "Alex", "Farrad",
#            "Vika", "Ruslan", "Erika"]
# Линейный поиск
# name = input("введите имя: ")
# found = False # Нужно для проверки
# for index in range(len(my_list)): # index это переменная от 0-6
#     if my_list[index] == name: # если имя в списке совпадает с указаным именем
#         print(f"{my_list[index]} найдено", index)
#         found = True # Имя найдено, переменная поменялась
#         break # Чтобы не проходили дальше, если уже нашли элемент
# if found == False: # Если переменная не поменялась, значит имя не нашлось
#     print("Имени нет в списке")


# Самый легкий способ
# if name in my_list:
#     print(my_list.index(name))





# import random
# computer = random.randint(1,100)
# count = 1
# while True:
#     user = int(input("угадайте число: "))
#     if user == computer:
#         print(f"Попытка {count}, угадали!")
#         break
#     elif user > computer:
#         print(f"Попытка {count}, должно быть меньше!")
#     elif user < computer:
#         print(f"Попытка {count}, должно быть больше!")
#     count += 1


# логарифм с базой 2 (100) это скорость алгоритма на 100 элементов





# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Функция бинарного поиска
# def binarySearch(my_list, num, low, high):
#     while low <= high:
#         mid = low + (high - low)//2 # индекс середины списка
#         if my_list[mid] == num:
#             return mid
#         elif my_list[mid] < num:
#             low = mid + 1 # начало списка станет на середине
#         else:
#             high = mid - 1 # конец списка станет на середине
#     return -1 # если элемент не найдет, выдаст -1
#
# my_list = [3, 4, 5, 6, 7, 8, 9]
# num = 4
# result = binarySearch(my_list, num, 0, len(my_list) - 1)
# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")




# Пример поиска через скрытый цикл
# my_list = ["Alex", "Farrad", "Bael", "Eliza", "Kanykei"]
# user = input("введите имя: ")
# if user in my_list: # Несмотря на то, что это if-else, цикл присутствует внутри программы
#     print(user)



# Напишите программу, которая принимает вес арбуза
# И проверяет делится ли он на 2 без остатка
# 10 -> 6 и 4
# 2 -> 1 - 1 (Нужно исключить)
# user = int(input("введите число: "))
# if user % 2 == 0 and user !=2:
#     print("YES")
# else:
#     print("NO")




# Часть 1
# Напишите программу, которая принимает 5 чисел
# И добавляет их в список
# Отсортируйте числа
# nums = []
# for element in range(5):
#     elem = int(input("введите число: "))
#     nums.append(elem)
# nums.sort()
# print(nums)



# Второй способ
# генератор списка
# nums = [int(input()) for element in range(5)]
# nums.sort()
# print(nums)


# Создайте список из нечетных чисел с 1 до 10
# Используя генератор списков
# my_list = [elem for elem in range(1,11) if elem%2!=0]
# print(my_list)






