# try: # Попробуем запустить код
#     print("hey")
#     1/0 # деление на 0 (приведет к ошибке)
# except: # поймаем ошибку, чтобы код не останавливался
#     print("на ноль делить нельзя")


# 1/0 -> Zerodivision error
# a + b -> Name error
# my_list[123] -> Index out of range
# "text" + 1 -> Type error
# int("hey") -> Value error


# Пример с иерархией ошибок в питоне
# my_list = {}
# try:
#     my_list["hey"]
# except LookupError: # общее название ошибки для индекса и ключа
#     print("hey")





# Пример нескольких исключений
# my_list = [1, "text", 0]
# for element in my_list:
#     try:
#         print(1/element)
#         print(my_list[123])
#     except ZeroDivisionError:
#         print("Ошибка деления на 0")
#     except TypeError:
#         print("Ошибка разных типов")
#     except:
#         print("любая другая ошибка")


# import sys # импорт системного модуля
#
# my_list = ["text", 0, 2]
# for elem in my_list:
#     try:
#         print("элемент", elem)
#         result = 1/int(elem) # пример кода ошибки
#     except:
#         print("Упс!", sys.exc_info()[0])
#     print()






# Пример вызова ошибки
# raise MemoryError("что-то память, как у рыбки")


# Пример с raise error
# try:
#     num = int(input("введите позитивное число: "))
#     if num > 0:
#         print("Все правильно, число:", num)
#     else:
#         raise ValueError(num, "НЕпозитивное число!")
# except ValueError as ve:
#     print(ve)



# Пример работы с else
# try:
#     print(1/1)
# except: # попробуем поймать ошибку, если она есть
#     print("какая-то ошибка")
# else: # работает, когда except не находит ошибок
#     print("Никаких ошибок")

# Пример с finally
# try:
#     print(x)
# except:
#     print("какая-то ошибка")
# finally: # выводит код в конце концов (неважно есть ошибка или нет)
#     print("Блок try-except закончился")





# Пример со всеми
# try:
#     print(1/1)
# except:
#     print("какая-то ошибка")
# else:
#     print("никаких ошибок")
# finally:
#     print("блок закончен")




# Создайте функцию, которая принимает 3 числа
# И выдает самое большое из них
# def max_num(a,b,c):
#     print(max(a,b,c))
# max_num(1,2,3)


# Альтернативный пример с сортировкой
# my_list = [1,2,3]
# my_list.sort(reverse=True)
# print(my_list[0])



# Напишите программу, которая принимает число
# И выводит длину числа
# len()
# num = input("введите число:")
# print(type(num)) # input сразу принимает в виде текста
# print(len(num)) # len не работает на числа




# без len(), посчитать количество чисел
# num = int(input("введите число: ")) # если вводимое число должно быть int
# num = str(num) # переводим в строку
# count = 0
# for elem in num: # проходимся по строке числа
#     count += 1
# print("длина:", count)





# Принимаем число, и нам нужно выдать количество цифр
# Не включая знаки типа минуса
# num = input("введите число: ")
# count = 0
# for elem in num:
#     if elem.isdigit(): # проверка, является ли элемент числом
#         count += 1 # если это число, то к длине +1
# print(count)









def students(**data):
    for key, value in data.items():
        print(key, ":", value)
    print()










