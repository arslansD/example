# Программа, для вывода четных чисел
# count = 1
# while count <= 30:
#     if count % 2 == 1:
#         print(count)
#     count += 1


# Второй способ
# count = 1 # число с которого мы начинаем
# while count <= 30: # условие работы цикла
#     if count % 2 != 0: # если число делится на 2, и в остатке дает НЕ 0
#         print(count) # выведем число (нечетное)
#     count += 1 # Для следующего шага, и для завершения циклы

# Третий способ
# count = 1
# while count <= 30:
#     print(count)
#     count += 2 # вы можете сами указать, сколько шагов пропустить


# Пример разного добавления в переменную цикла
# count = 0
# while count <= 1000: # 2000 <= 1000
#     print(count) # 0
#     count += 2000 # 2000


# False - 0 - НЕ является истиной
# True - любое число - истина
# while True:
#     print("hey")








# my_list = [1,2,3]
# for num in my_list: # 1 - 2 - 3
#     print(num)




# word = "hello"
# for letter in word: # для буквы в слове
#     print(letter) # выведите букву (по одной)




# my_list = [1,2,3,4,5,6,7,8,9,10]
# for num in my_list:
#     print(num)


# for num in range(100): # для числа в диапазоне 100 (от 0 до 99)
#     print(num)


# first = int(input("Введите начало: "))
# last = int(input("введите конец: "))
# for num in range(first, last+1): # Можно указать диапазон используя переменные
#     print(num)
# Ctrl + z (назад)
# ctrl + y (вперед)

# a = 0 # начало
# b = 1000 # конец (Он покажет ДО этого, т.е невключая это число)
# c = 25 # через сколько (перешагивает)
# for num in range(a,b,c):
#     print(num)





# a = 100 # Если число больше, чем конец
# b = 0
# c = -1 # то нужно добавить, какой шаг нам нужно сделать (в данном случае 1 шаг назад)
# for num in range(a,b,c): # от 100 до 0, при каждом шаге -1
#     print(num)



# my_list = ["проснуться", "поесть", "пойти на учебу"]
# print(my_list[0])
# count = 0 # начинаем с 0 индекса списка
# while count < len(my_list): # пока count меньше длины списка
#     print(my_list[count]) # выводим элемент на индексе count, из списка my_list
#     count += 1 # переходим к след шагу



# Пример вывода с for
# for task in my_list: # для какого-то дела в списке
#     print(task) # вывести дело



# word = "hello world"
# for letter in word:
#     if letter == "o": # если letter равен o,
#         break # то мы выходим из цикла
#     else:
#         print(letter)




# word = "hello world"
# for letter in word:
#     if letter == "o": # если letter равен o,
#         continue # то мы пропускаем данный шаг и начинаем новый
#     else:
#         print(letter, end = "")

# break - выходит из цикла полностью
# continue - перешагивает нынешний шаг, и продолжает цикл



# sentence = [1,2,3,4]
# for num in sentence:
#     print(num, end = " ") # выводим цифры в одну строку
#
# print(*sentence) # выводит элементы БЕЗ скобок, запятых, кавычек и т.д
#
# print(1,2,3) # покажет числа через пробел
# print(1,2,3, sep = ", ") # покажет числа через запятую
# print(1,2,3, end = ", ") # поставит запятую ТОЛЬКО в самый конец принта



# Создайте список из 5 имён
# выведите имена используя цикл for
# (и если сможете то и с циклом while)
names = ["Alex", "Farrad", "Vika", "Steven", "Rick"]
# for name in names:
#     print(name)


# Способ через while
# count = 0
# while count < len(names):
#     print(names[count])
#     count += 1






# Программа, которая принимает 5 имен
# И добавляет их в список
# my_list = []
# for num in range(1,6): # либо range(5)
#     name = input("введите имя: ") # принимаем имена
#     my_list.append(name) # добавляем имена
# print(my_list) # выводим список



# my_list = [] # пустой список
# while len(my_list) < 5: # пока длина списка меньше 5
#     name = input("введите имя: ") # принимаем имя
#     my_list.append(name) # добавляем имя
# print(my_list)

# KAHOOT.IT

s = 0
k = 2
while k < 10: # 11 > 10
    s += 2 * k # 4 # 14 # 30
    k += 3     # 5 # 8 # 11
print(s)

