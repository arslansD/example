# number = 5
# while number > 0:
#     number = number - 1
#     print(number)



# while True:
#     print("hello world")
#     break




# a = True
# b = False
# print(type(a))
# print(type(b))



# for lp in range(1, 25 + 1):
#     print(lp)




# word = "hello"
# for letter in word:
#     if letter == "e":
#         continue
#     print(letter)

# break - полностью выходит из цикла
# continue - пропускает шаг, и продолжает цикл
# pass - ничего не делает (просто для избежания ошибки в недописаном коде)





# print("hello", end = " ") # поставит пробел в конце слова
#
# for element in "hello":
#     print(element, end = " ") # h e l l o

# sep - делит отдельные элементы внутри одного print'a
# end - делит элементы разных print'ов




# Напишите код, который будет добавляет 1
# к переменной "c", каждый раз когда цикл проходится
# string="Civilization"
# c = 0
# for letter in string:
#     c = c + 1 # c +=1
# print(c) # вручную сколько букв
# print(len(string)) # проверка командой




# for num in range(1, 11): # от начала, до определенного элемента
#     print(num)


# for element in range(10): # от 0, до этого числа (не включительно)
#     print(element)


# for elem in range(0, 101, 10): # от начала, до конца, перешагивая сколько-то шагов
#     print(elem)

# for element in range(10, 0, -1): # 10 9 8 7
#     print(element)
# Если первый параметр больше второго, то цикл не сработает ни один раз
# Для нормальной работы цикла, нужно добавить третий аргумент
# который от первого числа будет отнимать шаг



# желательно пользоваться переменными, когда вы проходитесь через for
# my_list = [1,2,3]
# for i in my_list:
#     print(i)



# list comprehension
# my_list = [num for num in range(1,11)]
# print(my_list)


# тоже самое обычным способом
# my_list1 =[]
# for num in range(1,11):
#     my_list1.append(num)
# print(my_list1)