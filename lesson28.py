# Повторение классов-обьектов
# class Parrot:
#     # атрибут класса, статический атрибут
#     species = "bird"
#
#     def __init__(self, name, age): # атрибут обьекта, динамический атрибут
#         self.name = name
#         self.age = age
#
#     def sing(self, song):
#         return f"{self.name} sings '{song}'"
#
#     def dance(self):
#         return f"{self.name} is dancing"
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 12)
# print(blu.dance())
# print(blu.sing("happy"))

# print(f"Blu is a {blu.__class__.species}") # атрибуты обьекта поменялись, а атрибут класса остался
# print(f"Woo is a {woo.__class__.species}")


# Пример наследования
# class Bird:
#     def __init__(self):
#         print("Bird is ready")
#     def whoIsThis(self):
#         print("Bird")
#     def swim(self):
#         print("Swim faster")


# class Penguin(Bird):
#     def __init__(self):
#         super().__init__() # воспользовались функцией из род. класса
#         print("Penguin is ready")
#
#     def whoIsThis(self): # Перезапись (overriding)
#         print("Penguin")
#
#     def run(self): # Расширение (extending)
#         print("Run faster")
#
# peggy = Penguin()
# peggy.whoIsThis()
# peggy.swim()
# peggy.run()


# Пример инкапсуляции
# class Phone:
#     def __init__(self):
#         self.__price = 900
#     def getPrice(self): # Геттер - выдает информацию
#         print(self.__price)
#     def setPrice(self, price): # Сеттер - изменяет информацию
#         self.__price = price
# Nokia = Phone()
# Nokia.getPrice() # 900
# Nokia.setPrice(3000) # поменяли цену на 3000
# Nokia.getPrice() # показывает новую цену -> 3000







# Пример полиморфизма
# * - знак умножения пример
# print(10 * 123) # работает на числа
# print(3 * "hey") # работает на строки
# print(3 * [1,2,3]) # работает на списки
# print(3 * (4,5,6)) # работает на кортежи








# Задания на инкапсуляцию
# Создайте класс Person, и в методе init,
# Дайте ему имя - Пользователь
# Создайте обьект, и выведите имя
# class Person:
#     def __init__(self):
#         self.__name = "User" # __ защита от получения и изменения
#
#     def getName(self): # функция для получения имени
#         return self.__name
#
#     def setName(self,name): # функция для изменения имени
#         self.__name = name
# person1 = Person()
# print(person1.getName())
# person1.setName("Vika")
# print(person1.getName())







# Создайте класс, Dog, дайте ему 2 атрибута, 2 метода
# и метод __str__, чтобы показать всю информацию о собаке
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def speak(self):
        print("Гав Гав!")
    def hunt(self):
        print("охота")
dog1 = Dog("Sharik", "grey")
dog1.speak()
dog1.hunt()


