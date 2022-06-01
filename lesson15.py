# my_set = set() # создание пустого сета
# print(type(my_set))


# my_set1 = set([1,2,2,2,3,3,3]) # удалит дубликаты
# print(my_set1)


# my_set2 = {1,2,3}
# my_set2.add(4) # добавляет только 1 число
# print(my_set2)


# my_set3 = {1,2,3}
# my_set3.update([4,5,6]) # работает для коллекции
# print(my_set3)



# my_dict = {"name":"Tyler",
#            "age": 123,
#            "hobby": "singing"}
# print(my_dict["name"]) # Только один ключ можно писать при выводе



# my_dict = {"name":"Jack",
#            "age":27}
# print(my_dict["name"]) # вывод через ключ и скобки
# print(my_dict.get("name")) # вывод через команду

# print(my_dict["address"]) # если ключа не существует, то ошибка
# print(my_dict.get("address")) # Если ключа нет, то просто None


# my_dict = {"name":"Jack",
#            "age":27}
# my_dict["address"] = "Downtown" # добавление несуществуего адреса
# print(my_dict.get("address"))

# my_dict["address"] = "Uphill" # изменение адреса на другой
# print(my_dict.get("address"))



my_dict = {"name":"Jack",
           "age":27}

# my_dict.pop("age") # удаление и возврат через pop и ключ
# del my_dict["age"] # удаление через del и ключ

# print(my_dict.popitem()) # удаляет и возвращает последнюю пару ключ-значение
# print(my_dict.pop('name')) # удаляет из возвращает значение

# my_dict.clear() # очищает словарь, но сама переменная существует
# print(my_dict)






# Создайте словарь с любимым фильмом
# и подробностями о нем (Примерно 5)
film = {"title": "Shutter Island",
        "genge":"thriller",
        "actors":["Di Caprio", "zxc"],
        "year":2007,
        "rating": 7.8
        }
for key in film:
    print(key,"-", film[key])

# Используя команды, поменяйте одно значение (Через присваивание)
# Добавьте новую пару ключ-значение (Через равно)
# удалите одно из старых значений (Через del, pop, popitem)
# film["rating"] = 9.9 # изменили старое значение
# film["budget"] = 123
# del film["genge"] # удалили ключ и значение жанр
# film.pop("actors") # удалили (И вернули) ключ и значение actors
# film.popitem() # удаляет (и возвращает) последний элемент
# print(film)











