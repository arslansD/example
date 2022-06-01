# def info(name):
#     print(name)
# info("Farrad")
#
# def info2(name):
#     return name
# print(info2("Vika"))





# def adder(x,y,z):
#     print(x + y + z)
# adder(10,11,12) # Функция, принимает ровно столько аргументов, сколько параметров указано


# nums = (1,2,3) # Пример вывода из кортежа
# for element in nums:
#     print(element)



# def adder(*nums):
#     summary = 0
#     for element in nums: # проходимся по кортежу
#         summary += element
#     print("сумма:", summary)
# adder(1,2,3) # Неважно сколько аргументов, он складывает числа


# def info(**data):
#     for key, value in data.items():
#         print(key, value)
# info(title = "shutter Island", actor = "Leo Dicaprio", budget = 123)
# # при вызове функции, ключи должны быть БЕЗ кавычек

# my_dict = {"title": "Avengers"} # в словарях, надо ставить ключи в кавычки
# print(my_dict)


# def students(*names): # вывод имен через args
#     for name in names: # для имени внутри кортежа имен
#         print(name) # выводим одно имя
# students("Farrad", "Aiana", "Alex")



# def students(): вывод имен через input и БЕЗ аргументов
#     names = input("введите имена: ").split()
#     print(names)
#     for element in names:
#         print(element)
# students()




# def employee(name, age=20): # условный значение возраста
#     print(name, age)
# employee("Farrad")

# def greet(name = "пользователь"): # условный аргумент
#     print("Добро пожаловать", name)
# greet("Farrad")




# def info(*args, **kwargs): # Пример использования args и kwargs одновременно
#     print(args)
#     print(kwargs)
# info("Alex", "Farrad", name = "hey")





# Напишите функцию, которая принимает неизвестное количество
# чисел, и выводит эти же числа деленые на 2
# def divide(*nums):
#     for element in nums: # для какого-то числа (element) внутри кортежа (1,2,3,4)
#         print(element/2) # берем число и делим на 2
# divide(1,2,3,4)



# Создайте функцию, которая принимает неизвестное количество
# чисел. Выводит только четные числа
# def even(*numbers):
#     for num in numbers:
#         if num % 2 == 0: # проверяем каждое отдельное число на четность
#             print(num)
# even(1,2,3,4,5,6)

# Напишите программу, которая проходится по списку
# Сравнивает элементы с "neolabs", если пароль равен
# выдает "Можно!", если не равен выдает "нельзя!"

passwords = ["neo", "hey", "check", "neolabs"]
secret = "neolabs"
# for element in passwords:
#     if element == secret:
#         print("yes")
#     else:
#         print("nope")


# Второй вариант (показывает только 1 раз)
# if secret in passwords:
#     print("yes")
# else:
#     print("no")

import antigravity
