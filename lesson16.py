# my_dict = {} # создание словаря
# print(type(my_dict))

# my_set = set() # создание множества (сет)



# student = {"name": "Alex",
#            "age": 123,
#            "hobbies":["reading", "swimming", "sleeping"],
#            "favourite music": ["Linkin Park", "Twenty One Pilots", "AC/DC"],
#            "favourite films": ["Shutter Island", "Harry Potter", "Spiderman"]
#            }
# print(*student["hobbies"], sep= ", ")

# for key in student: # Вывод через ключ
#     print(key, student[key]) # вывод ключей и значений

# for key, value in student.items():
#     if type(value) == list:
#         print(key, ":", *value)
#     else:
#         print(key, ":", value)




# my_list = [1,2,3]
# my_list.remove(2) # удаление по элементу в списке


# my_dict = {"country": "Kyrgyzstan",
#            "capital": "Bishkek",
#            "cities": ["Bishkek", "Talas", "Naryn", "Karakol"]}

# del my_dict["capital"] # удаляет навсегда
# value = my_dict.pop("country") # удаляет из словаря, и сохраняет в переменной
# key_value = my_dict.popitem() # удаляет из словаря, и сохраняет пару ключ-значение в переменной

# my_dict["capital"] = "Naryn" # Присвоение нового значения
# my_dict["region"] = "Central Asia" # добавление нового ключа-значения в конец словаря
# my_dict["cities"].append("Osh") # append работает, потому что мы работаем со списком
# print(my_dict)


# Создайте пустой словарь, и используя команды input(),
# добавьте туда ключи и значения (4 пары)
# books = {}
# user = int(input("введите количество попыток: "))
# for element in range(user): # первый способ записи
#     key = input("введите ключ: ")
#     value = input("введите значение: ")
#     books[key] = value # способ добавления
# print(books)

# второй способ записи
# count = 0
# while count < 4:
#     key = input("введите ключ: ")
#     value = input("введите значение: ")
#     books[key] = value  # способ добавления
#     count += 1 # считает шаг (и в конце остановит цикл)
# print(books)
#
# for item in books.items(): # Вывод в столбик
#     print(*item, sep = " : ")



books = {"title": "power of will",
         "author": "Kelly",
         "year": 2016}
user = int(input("введите количество попыток: "))
for element in range(user): # первый способ записи
    operation = input("удалить или добавить (app/del): ").lower() # Принимаем команду
    if operation == "del": # проверяем команду на удаление
        key = input("введите какой ключ удалить: ")
        del books[key]
        print(books)
    elif operation == "app":    # пропишите код для добавления пары ключ-значение
        key = input("введите какой ключ добавить: ").lower()
        value = input("введите какое значение добавить: ")
        books[key] = value
        print(books)
    else:
        print("Ввод неверен, попытка сгорает!")
