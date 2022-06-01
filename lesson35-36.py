# ДЗ по алгоритмам
# while True:
#     user = int(input("введите пароль: "))
#     if user == 2016:
#         print("Access permitted")
#         break
#     else:
#         print("incorrect password")



# задание 5 из теста
# a = int(input())
# b = int(input())
# if a%10 == 0 or b % 10 == 0:
#     print("YES")
# else:
#     print("NO")


# Задание 6
# print(7//3 + 7//-3)
# 0 1 2 x 3 4
# print(7//3) # округляет в меньшую сторону -> 2
# print(7//-3) # округляет в меньшую сторону -> -3
# -3 x -2 -1 0





# num = 2,3
# print(type(num)) # кортеж



# num = 2
# print(float(num)) # добавляет точку

# задание 11
# my_tuple = ("",) # заметьте запятую
# print(type(my_tuple))






# coordinates = int(input("введите координаты: "))
# step = 0
# while coordinates > 0:
#     coordinates -= 5 # 2 - 5 = -3
#     step += 1 # 2 + 1 = 3
# print(step)



# Способ через двойное деление
# elephant = int(input("Сколько клеток"))
# count = 0
# steps = elephant//5
# if elephant % 5 == 0:
#     print(steps)
# else:
#     print(steps+1)


# Способ через двойное деление + остаток
# distance = int(input())
# print(distance//5 + (distance%5>0)) # Тоже самое, что выше, но в одну строчку



# Псевдокод бинарного поиска
# массив - [...]
# start - начало_диапазон_поиска
# end - конец_диапазона
# mid_num - центральный_элемент_диапазона
# search_num - входное_число_которое_нужно_найти
# not_found - Правда(число_не_найдено)

# до тех пор пока start больше_равно end:
#      если search_num равен mid_num то:
#           вывод(число найдено на индексе mid_num)
#           not_found - Ложь(число_найдено)
#           (остановить цикл)
#
#      или если search_num больше mid_num то:
#           start - mid_num
#
#      или если search_num меньше mid_num то:
#           end - mid_num
#
# если not_found то:
# вывод(числа нет в массиве)




# user = input().split()
# user = list(map(int, user)) # превращает все элементы в целые числа
# summary = 0
# for element in user:
#     summary += element # считает сумму чисел
# print(summary)



# задание 19 из теста
# class Person:
#     def __init__(self, name, age): # динамические атрибуты
#         self.name = name
#         self.age = age
#
#     def run(self): # методы - поведение
#         print("человек бежит")
#
#     def chill(self):
#         print("человек лежит на диване")
# person1 = Person("Farrad", 123)
# print(person1.name, person1.age)
# person1.run()
# person1.chill()





# Задание 20
# def info(*data):
#     for word in data:
#         print(word)
# info("Hello", "hiya", "hi")








# Создайте класс растение, у которого есть 2 атрибута
# и два метода
# class Plant:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def grow(self):
#         print("растем")
#
#     def photosynthesis(self):
#         print("фотосинтезирую")
# holand_rose = Plant("Голадская роза", "красный")
# print(holand_rose.name, holand_rose.color)
# holand_rose.grow()
# holand_rose.photosynthesis()




# Пример наследования
# class Person: # род. класс
#     def eat(self):
#         print("вкусно поедим")
#
# class Doctor(Person): # дочерний класс
#     def cure(self): # расширение - extending
#         print("лечить")
#
#     def eat(self): # перезапись - overriding
#         print("На работе есть нельзя")
#
# doctor1 = Doctor()
# doctor1.eat()


# Инкапсуляция
# class Computer:
#     def __init__(self):
#         self.__price = 2000
#
#     def getPrice(self): # геттер для получения информации
#         print(self.__price)
#
#     def setPrice(self, price): # сеттер для изменения информации
#         self.__price = price
#
# laptop = Computer()
# laptop.getPrice()
# laptop.setPrice(3000)




# Самый легкий пример полиморфизма
# print(5 * 5)
# print(5 * "5")
# print(5 * [1,2,3])
# print(5 * (4,5,6))


# Уже готовый концепт полиморфизма
# class Mercedes:
#     def drive(self):
#         print("разгоняется со скоростью 100 км за 2 сек")
#
# class BMW:
#     def drive(self):
#         print("разгоняется со скоростью света")
#
# obj1 = Mercedes()
# obj2 = BMW()
# my_garage = [obj1, obj2]
# for car in my_garage:
#     car.drive()

# Fn + shift + F6 -> для изменения переменной везде в файле