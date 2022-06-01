# with open("lesson32.txt", "x", encoding="utf-8") as file:
#     file.write("qwerty")

# x - эксклюзивное создание, которое работает только если файл не существует
# with open("lesson32.txt", "w", encoding="utf-8") as file:
#     file.write("hey\n")
#     file.write("hiya\n")
#     file.write("stop\n")


# открываем файл для чтения
# with open("lesson32.txt", "r", encoding="utf-8") as file:
#     print(file.read(4))


# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     print(file.read(4))
#     file.write("hey")
# Если написать мод через +, то можно выполнить несколько команд




# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     print(file.read(100))
# если выбрать большое число, то покажет до конца файла



# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     file.seek(3) # переносит курсор
#     print(file.tell()) # показывает позицию



# Цикл в файлах
# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     for line in file: # пройтись по каждой строке в файле
#         print(line) # вывести строку


# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     print(file.readline()) # выводит одну строку


# коротко о выводе всего файла
# with open("lesson32.txt", "r+", encoding="utf-8") as file:
#     print(file.readlines()) # список нескольких строк, можно использовать команды списка
#     print(file.read()) # одна большая строка, можно использовать команды строки



# откройте файл для записи, и добавьте туда
# числа от 1 до 100
# with open("lesson32.txt", "w", encoding="utf-8") as file:
#     for num in range(1, 101):
#         file.write(f"{num}\n")

# сумма чисел в файле
# with open("lesson32.txt", "r", encoding="utf-8") as file:
#     summary = 0
#     for element in file:
#         summary += int(element)
#     print(summary)


# Второй способ ввиде встроенных функции в одну строку
# with open("lesson32.txt", "r", encoding="utf-8") as file:
#     print(sum(list(map(int, file.read().split()))))



# Второй способ разделенный на разные строки
# with open("lesson32.txt", "r", encoding="utf-8") as file:
#     my_str_list = file.read().split() # список строк
#     my_int_list = list(map(int, my_str_list)) # список чисел
#     total = sum(my_int_list)
#     print(total)




# Закинуть питон код в другой файл, и импортировать его обратно
# with open("lesson32test.py", "w", encoding="utf-8") as file:
#     file.write(f'''class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def speak(self):
#         print("Гав Гав!")
#     def hunt(self):
#         print("охота")''')
# from lesson32test import *
# dog1 = Dog("Kuzya", "brown")
# print(dog1.name, dog1.color)
# добавьте любую функцию, либо класс в новый файл
# и импортируйте его назад



# Разница между режимами при открытии файла
# W - Write - написать (перезаписать)
# A - Append - Добавить (добавить к существующему)
# X - eXclusive - исключающий (создает файл, если его не существует)
# R - read - прочитать (показывает содержимое файла)
# \n - New line (Новая строка)




# маленькая программа на проверку слов юзера
# with open("lesson32.txt", "r", encoding="utf-8") as file:
#     user = input("введите текст: ")
#     for word in file.read().split():
#         if word in user:
#             user = user.replace(word, "*"*len(word))
#     print(user)
