# ДЗ 27-28, задание 1
# class Jet:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def fly(self):
#         print("Самолет летает")
#
#     def accelerate(self):
#         print("Самолет разгоняется")
# jet1 = Jet("F14", 2004)
# print(jet1.name, jet1.year)
# jet1.fly()
# jet1.accelerate()


# Задача 2
# class Bank:
#     def __init__(self):
#         self.__money = 2000
#
#     def getMoney(self): # геттер для получения информации
#         print("Денег на балансе", self.__money)
#
#     def setMoney(self, money): # Сеттер для изменения информации
#         self.__money = money
# account = Bank()
# account.setMoney(12345)
# account.getMoney()









# Оператор умножения для примера Полиморфизма
# print(3 * 10) # неважно какой тип данных, знак умножения работает
# print(3 * 3.14)
# print(3 * "hey")
# print(3 * [1,2,3])
# print(3 * (4,5,6))


# class Dog:
#     def speak_dog(self):
#         print("Гав гав!")
#
# class Cat:
#     def speak_cat(self):
#         print("Мяу мяу")
#
# class Duck:
#     def speak_duck(self):
#         print("кря кря")

# dog1 = Dog()
# cat1 = Cat()
# duck1 = Duck()
# animals = [dog1, cat1, duck1]
# for animal in animals:
#     if isinstance(animal, Dog):
#         animal.speak_dog()
#     elif isinstance(animal, Cat):
#         animal.speak_cat()
#     elif isinstance(animal, Duck):
#         animal.speak_duck()




# Если делать это с полиморфизмом
# class Dog:
#     def speak(self):
#         print("Гав гав!")
# class Cat:
#     def speak(self):
#         print("Мяу мяу")
# class Duck:
#     def speak(self):
#         print("кря кря")
# dog1 = Dog()
# cat1 = Cat()
# duck1 = Duck()
# my_list = [dog1,cat1,duck1]
# for animal in my_list:
#     animal.speak()






class Square:
    def __init__(self, side):
        self.side = side

    def area_figure(self): # узнаем площадь квадрата
        return self.side * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_figure(self): # площадь круга
        return 3.14 * self.radius ** 2

class Romb: # ромб
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area_figure(self): # площадь ромба
        return self.side1 * self.side2 / 2
square1 = Square(5) # объекты класса квадрат
square2 = Square(3)

circle1 = Circle(4) # объекты класса круг
circle2 = Circle(123)

romb1 = Romb(4,5) # объекты класса ромб
romb2 = Romb(6,7)
my_list = [square1, square2, circle1, circle2, romb1, romb2]
for figure in my_list:
    # if isinstance(figure, Square): # этот код если полиморфизма нет
    #     print(figure.area_square())
    # elif isinstance(figure, Circle):
    #     print(figure.area_circle())
    # elif isinstance(figure, Romb):
    #     print(figure.area_romb())
    print(figure.area_figure()) # при полиморфизме

