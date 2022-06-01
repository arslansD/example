# Проверка ДЗ
# nums = input().split() # Принимаем числа через пробел
# nums = list(map(int, nums)) # Превращаем их в числовой тип
# if nums[0] != nums[1]:
#     print(nums[0] + nums[1])
# else:
#     print((nums[0] + nums[1]) * 2)


# Второй способ
# numbers = input().split() # Принимаем числа через пробел
# num1 = int(numbers[0]) # Даем названия числам
# num2 = int(numbers[1])
# if num1 != num2: # Если числа разные, то сумма
#     print(num1 + num2)
# else: # если одинаковые, то сумма * 2
#     print((num1+num2) * 2)



# my_list = ["сходить в магазин", "прийти домой", "приготовить еду"]
# my_list.append("хей")
# print(my_list[0])

# И список и кортеж упорядочены

# my_tuple = ("сходить в магазин", "прийти домой", "приготовить еду")
# my_tuple.append("hey")
# print(my_tuple[0])



# my_set = {1,1,1,2,2,2}
# # print(my_set[0]) # у сеты нельзя взять индекс
# my_set.add(3) # Множества изменчивы (можно добавить и удалить)
# print(my_set)


# В словарях мы храним информацию, и обращаемся по ключу
# my_dict = {"login": "Alex",
#            "password": "Farrad",
#            "double-check": "123"}
# print(my_dict)
# print(my_dict["login"])

# способы создания списка
# my_list1 = []
# my_list2 = list()
# print(type(my_list1))
# print(type(my_list2))




# my_list3 = [2, 3.14, True, "text", (), [], {}]
# for element in my_list3: # проверим, какого типа данных каждый элемент внутри
#     print(type(element))


# my_list4 = [1,2,3]
# del my_list4[0] # удаление
# my_list4.append(4) # добавление
# my_list4.pop(1) # вытащить из списка
# print(my_list4)



# queue (Очередь)
# FIFO - First In First Out
# к примеру, элемент на 0 индексе


# Stack (стэк)
# LIFO - Last In First Out
# к примеру, команда pop() вытаскивает элемент на последнем индексе



# import array as arr # в питоне массивы нужно импортировать
# array_1 = arr.array("i", [3, 6, 9, 12]) # тип данных int
# print(array_1)
# print(type(array_1)) # Тип данных массив





# import numpy as np
# array = np.array([3, 6, 9, 12])
# division = array/3 # С массивом так можно
# print(division)
# print (type(division)) # Массив из библиотеки numpy


# Со списками нельзя использовать математические операции (напрямую)
# my_list5 = [3,6,9,12]
# print(my_list5/3) # Выдаст ошибку, со списком нельзя



#1) Удалите 1 страну
#2) Добавьте Японию
#3) С помощью цикла показать сколько букв
# countries = ["Russia", "China", "USA"]
# del countries[0]
# countries.append("Japan")
# for country in countries:
#     print(country, len(country))



# Второй способ
# countries = ["Russia", "China", "USA"]
# for country in countries: # берем страны из списка
#     count = 0 # пока мы не считаем буквы
#     for letter in country: # берем буквы из одной страны
#         count += 1 # считаем каждую букву
#     print(country, count) # выводим страну и буквы




# Выведите список наоборот
# использовать pop(), и append()
# nums = [500,400,300,200,100]
# nums1 = []
# for element in range(len(nums)):
#     elem = nums.pop()
#     nums1.append(elem)
# print(nums1)

# Другие способы list(reversed())
# print(list(reversed(nums))) # выводит отсортированный список 1 раз

# Способ через reverse()
# nums.reverse() # меняет список навсегда
# print(nums)

# Способ через сортировку
# nums.sort() # простая сортировка списка
# print(nums)


# Способ через срезы
# print(nums[::-1]) # показывает числа в обратную сторону через срезы




# Напишите код, который вернет все строки в числа (int)
# либо, добавит их в другой список в виде чисел
# nums1 = ["500", "400", "300", "200", "100"]
# nums1 = list(map(int, nums1))
# print(nums1)

# Второй способ
# nums2 = []
# for element in nums1:
#     nums2.append(int(element))
# print(nums2)

# 1, 4, 9, 16, 25, 36, 49 вывести числа таким образом
multi = [1, 2, 3, 4, 5, 6, 7]
for num in multi:
    print(num ** 2, end = ", ")
