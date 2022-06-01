# Пример 1 для вывода имени
# class Jets:
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
# first_item = Jets("F16", "USA")
# a = first_item.name
# print(a)


# # Пример с выводом, когда есть одинаковые имена
# class Jets:
#     model = None # статические атрибуты класса
#     country = 0
#     def __init__(self, name, country): # динамические атрибуты
#         self.name = name
#         self.origin = country
# # F14, SU33, AJS37, Mirage2000, Mig29, A10
# first_item = Jets("F16", "USA")
# second_item= Jets("SU33", "Iraq")
# third_item= Jets("AJS37", "Iran")
# fourth_item= Jets("Mirage2000", "UK")
# fifth_item= Jets("Mig29", "Russia")
# sixth_item= Jets("A10", "Kyrgyzstan")

# first_army=[first_item,second_item,third_item,fourth_item,fifth_item,sixth_item]
# for element in first_army:
#     print(element.name)


# Пример добавления нового параметра
# class Jets:
#     model = None
#     country = 0
#     def __init__(self, name, country, quantity):
#         self.name = name
#         self.origin = country
#         self.quantity = quantity
#
# # F14 and Mirage2000 with quantities 87 and 35.
# first_item= Jets("F14", "USA", 87)
# second_item= Jets("Mirage2000", "Iraq", 35)
#
# total= first_item.quantity + second_item.quantity # -> 87 + 35
# print(total)




# Дописать класс, смотря на обьект
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#
#     def __str__(self):
#         return f"категория: {self.category}, год: {self.year}, победитель: {self.winner}"
#
# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)
# print(np2005) # обращение к обьекту через method __str__



# Создайте класс Myfunc, с одной функцией, которая называется fifth(x)
# Функция выдает это же число, в степени 5
# class Myfunc:
#     def fifth(x):
#         return x ** 5
#
# ans = Myfunc.fifth(5)
# print(ans)




# Создайте класс Doctor, дайте ему 2 атрибута, 2 метода

# И метод __str__, для вывода всей информации о обьекте
# class Doctor:
#     def __init__(self, name, qualification):
#         self.name = name
#         self.qualification = qualification
#
#     def cure(self):
#         print("доктор лечит")
#
#     def sleep(self):
#         print("Доктор спит")
#
#     def __str__(self):
#         return f"Имя: {self.name}, квалификация: {self.qualification}"
# doctor1 = Doctor("Farrad", "master")
# print(doctor1)
# doctor1.cure()
# doctor1.sleep()





