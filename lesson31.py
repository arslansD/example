# ДЗ наследование
# class Dog: # родительский класс dog
#     def speak(self):
#         print("Woof woof!")
#
#     def run(self):
#         print("бегу-бегу")
#
# class Husky(Dog):
#     def run(self): # перезапись - overriding
#         print("Мчусь!")
#
#     def crazy(self): # расширение - extending
#         print("смотрите на мои лапищи")
#
# dog1 = Husky()
# dog1.speak()
# dog1.run()
# dog1.crazy()


# ДЗ Полиморфизм
# class Cat:
#     def speak(self):
#         print("Meow Meow!")
#
# class Parrot:
#     def speak(self):
#         print("Иван дурак")
#
# class Dog:
#     def speak(self):
#         print("Woof woof!")
#
# cat1 = Cat()
# dog1 = Dog()
# parrot1 = Parrot()
# my_list = [cat1, dog1, parrot1]
# for animal in my_list:
#     animal.speak()


# Создайте класс Potato, дайте ей
# изначальную цену 500 (инкапсулированную)
# Создайте геттер и сеттер для просмотра,
# и изменения цены
# class Potato:
#     def __init__(self):
#         self.__price = 500
#     def getPrice(self):
#         print(self.__price)
#     def setPrice(self, price):
#         self.__price = price
# potato1 = Potato()
# potato1.getPrice()
# potato1.setPrice(1000)
# potato1.getPrice()



# r - read - прочитать
# w - write - перезапись
# a - append - добавить

# Пример проверки самых популярных паролей
# f = open("lesson31passwords.txt", "r", encoding="utf-8")
# user = input("введите пароль: ")
# if user in f.read().split("\n"):
#     print("это плохой пароль, придумайте новый")
# f.close()

# print(type(f.read())) # класс str



# try:
#     f = open("lesson31.txt") # Открывает файл для работы
#     print(f.read())
# finally:
#     f.close() # закрывает независимо от ошибки


# Самый удобный способ для открытия/закрытия файла
# with open("lesson31.txt", "r", encoding="utf-8") as file:
#     print(file.read())



# with open("lesson31.txt", "w", encoding="utf-8") as file:
#     file.write("qwerty")

