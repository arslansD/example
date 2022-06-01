# def info(name):
#     print(name) # Выводит имя
# info("Farrad")

# Вариант 2
# def info(name):
#     return name # сохраняем где-то имя
# print(info("Farrad")) # Выводим через print


# ДЗ Урок-19 задача 2
# def calculation(a,b):
#     print("Сумма:", a+b)
#     print("Разность:", a-b)
# calculation(10,15)
# # Лучше использовать print, т.к return сразу выходит из функции






# ДЗ-20 задача 1
# def odd_or_even(num):
#     if num % 2 == 0: # проверка на четность
#         print("even")
#     else:
#         print("odd")
# odd_or_even(4)



# ДЗ-20 задача 2

# def show_student(name, grade = 100): # прописали дефолтный параметр
#     print(f"Студент(ка) {name}, Оценка {grade}")
# show_student("Farrad")






# def students(**data): # Пример ключевых функции
#     for key, value in data.items():
#         print(f"{key} - {value}")
# students(name = "Ruslan", grade = 99)


# Пример границы 1
# def num():
#     global x # указываем, что x общедоступная переменная
#     x = 5
# num() # обязательно сначала вызвать, чтобы код внутри начал работать
# print(x) # теперь мы можем вывести значение из под функции



# Пример границы 2
# def show():
#     print(y)
# y = 5 # главное, чтобы переменная стояла ДО вызова функции
# show()


# Пример границы 3
# x = 5
# def numbers():
#     x = 6 # переменные созданные внутри функции, имеют больший приоритет для функции
#     print(x)
# numbers() # выводит 6, потому что относится к функции
# print(x) # выводит 5, потому что не видит переменную внутри функции







# Напишите функцию, которая принимает неизвестное количество
# ключевый аргументов (словарь данных о фильме)
# выведите эти данные через циклы
# def show(**film):
#     for key, value in film.items():
#         print(f"{key} : {value}")
# show(title = "shutter island", year = 123, actor = "Leo")



my_dict = {"название": None,
           "год": None,
           "жанр": None}
# for element in my_dict.keys(): # то как это видит клиент
#     client = input(f"введите {element} фильма: ")
#     my_dict[element] = client
# print(my_dict)

# то как это видит разработчик
# def show(data): # data это словарь
#     for key, value in data.items():
#         print(key, value)
# show(my_dict)







# Создайте функцию,
# которая создает список из чисел с 1 до 30
# my_list = list(range(1,31)) # первый способ используя уже известные функции
# print(my_list)

# Второй способ, делать это напрямую
# def contain():
#     my_list = []
#     for element in range(1,31):
#         my_list.append(element)
#     print(my_list)
# contain()


# List comprehension - Списковое включение
# my_list = [element for element in range(1,31)]
# print(my_list)


# Пример 2, использование цикла с другими элементами
# my_list = [input("введите дело: ") for element in range(3)]
# print(my_list)




# HoUse -> house
# maTRIx -> matrix
# ViP -> VIP
text = input("введите текст: ")
low = 0
high = 0
for letter in text:
    if letter == letter.lower():
        low += 1
    elif letter == letter.upper():
        high += 1


if high > low:
    print(text.upper())
else:
    print(text.lower())