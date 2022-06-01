# class Cat:
#     def __init__(self,name, cat_type): # динамические атрибуты
#         self.name = name
#         self.cat_type = cat_type
#     def speak(self): # методы класса
#         print("Meow Meow!")
#     def sleep(self):
#         print("Zzzzz")
#     def __str__(self): # для вывода обьекта в виде строки
#         return f"name: {self.name}, type: {self.cat_type}"
# cat1 = Cat("Пушок", "британский")
# print(cat1)
# cat1.speak()
# cat1.sleep()



# Пример-1 наследование
# class Person:
#     def walk(self): # функция род. класса
#         print("человек ходит")
#
# class Doctor(Person):
#     def cure(self): # функция доч. класса
#         print("Доктор лечит")
#
# doctor1 = Doctor() # обьект класса доктор может пользоваться функциями чел. класса
# doctor1.cure()
# doctor1.walk()


# Пример-2 наследование от нескольких классов
# class Predator: # род. класс хищник
#     def hunt(self):
#         print("hunting")
# class Wolf: # род. класс волк
#     def howl(self):
#         print("ААуууууууууу!")
# class Dog(Wolf, Predator): # доч. класс собака, который наследует от хищника и волка
#     def hunt(self):
#         print("Собака не охотится")
# dog1 = Dog()
# dog1.hunt()
# dog1.howl()
# обьект -> класс -> род. класс



# class Bird:
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print("птица летит")
# class Penguin(Bird):
#     def __init__(self,name):
#         super().__init__(name)
#     def fly(self): # overriding - Перезапись
#         print("Пингвины не летают")
#     def swim(self): # extending - расширение
#         print("хорошо плавают")
# pepe = Penguin("pepe")
# print(pepe.name)
# pepe.fly()
# pepe.swim()




# Пример-3 сайт
# class Jets:
#     def __init__(self, name, country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
#
# class F14(Jets):
#     def __init__(self):
#         self.name = "F14"
#         self.origin = "USA"
#
# a = F14()
# print(a.origin)
# print(a.name)



# Пример-4 с сайта
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
#
# class F14(Jets):
#     def __init__(self):
#         self.name = "F14"
#         self.origin = "USA"
#         self.engine = 2
#         self.seat = 2
#         self.tail = 2
#         self.speed = 2
#
# a = F14()
# print(a.engine)
# print(a.seat)


# Пример-5 с сайта
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.type = "Jet"
#         self.area = "Air"
#         self.name = name
#         self.origin = country
#
# class AJS37(Jets):
#     def __init__(self):
#         self.name = "AJS37"
#         self.origin = "Sweeden"
# ajs = AJS37()
# print(ajs.name)
# print(ajs.origin)



# Создайте класс Feline, и дайте ему два атрибута и 2 метода
# Создайте класс House_cat, дайте ему два дефолтных атрибута,
# И один метод поменяйте, и один добавьте
# class Feline:
#     def __init__(self,name, color):
#         self.name = name
#         self.color = color
#     def hunt(self):
#         print("кошка охотится")
#     def speak(self):
#         print("Meow meow!")
#
# class House_cat(Feline):
#     def __init__(self,name, color):
#         super().__init__(name, color)
#     def hunt(self): # overriding-перезапись
#         print("жду корм")
#     def sleep(self): # extending - расширение
#         print("всегда спит")
# cat1 = House_cat("Пушок", "белый")
# cat1.speak()
# cat1.hunt()
# cat1.sleep()
# print(cat1.name, cat1.color)
