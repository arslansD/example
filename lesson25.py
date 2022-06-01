# class MotorTransport:
#     # Свойства - описание - атрибуты - харакристика
#     def __init__(self, color, year, auto_type):
#         self.color = color
#         self.year = year
#         self.auto_type = auto_type
#
#     # Методы - поведение - функции
#     def stop(self):
#         print("останавливаемся")
#
#     def drive(self):
#         print("Врум-врум!")

# обьект - экземпляр - пример
# ferrari = MotorTransport("purple", 2016, "passeger car")
# ferrari.drive()
# ferrari.stop()
# print(ferrari.year, ferrari.color, ferrari.auto_type)





# class Student:
#     def __init__(self, name, surname, group):
#         self.name = name
#         self.surname = surname
#         self.group = group
#
#
# alex = Student("Alex", "Farrad", "admin")
# print(alex.name, alex.surname, alex.group, sep = ", ")



# class MightiestWeapon:
#     name = "default name" # статический атрибут
#     def __init__(self, weapon_type):
#         self.weapon_type = weapon_type
#
# deagle = MightiestWeapon("Long-range")
#
# print(MightiestWeapon.name) # Вызвали через КЛАСС, потому что статический
# print(deagle.weapon_type) # Вызвали через ОБЬЕКТ, потому что динамический











# Создайте класс Person, с 3 атрибутами, и 3 методами
# Создайте обьект класса, и проверьте работоспособность

# class Person:
#     def __init__(self, name, surname, age): # Три атрибута для описания человека
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     # Три метода, что человек может делать
#     def sleep(self):
#         print("засыпает")
#
#     def eat(self):
#         print("время поесть")
#
#     def walk(self):
#         print("пора походить")
#
#     def info(self): # Метод чтобы вывести все
#         print(self.name)
#         print(self.age)
#         print(self.surname)

# person1 = Person("Farrad", "Alex", 123)
# person1.info()
# person1.eat()
# person1.sleep()
# person1.walk()








# Создайте класс Bird, и дайте 3 атрибута, и 3 метода
# Создайте обьект данного класса, и проверьте
# class Bird:
#     def __init__(self, age, bird_type, color):
#         self.age = age
#         self.bird_type = bird_type
#         self.color = color
#
#     def fly(self):
#         print("могу летать")
#
#     def hunt(self):
#         print("охотится")
#
#     def voice(self):
#         print("Чирик-чирик")
#
# bird1 = Bird(4, "hunting bird", "black")
# print(bird1.age, bird1.bird_type, bird1.color)
# bird1.hunt()
# bird1.voice()
# bird1.fly()

