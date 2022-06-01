# ДЗ-урока 5
# total = int(input("введите количество уроков: "))
# attended = int(input("введите сколько уроков вы посещали: "))
# formula = attended/total * 100
# if formula >= 75:
#     print("Разрешено", round(formula))
# else:
#     print("Запрещено")


# candy = 10 # общее количество конфет
# while candy > 0: # условие цикла
#     print("едим конфеты", candy)
#     candy = candy - 1 # для того, чтобы цикл закончился, нам нужно отнимать от общего количества конфет


# Пример-2: вывести числа с 1 до 20
# count = 1
# while count <= 20: # условие
#     print(count)
#     count += 1 # к переменной добавляем 1
# print("end of loop") # покажет только 1 раз, т.к не относится к циклу


# count = 0 # для проверки шага в условии
# total = 0 # храним сумму
# while count < 100: # 1, 2, 3...     (99 < 100)
#     count += 1 # продолжаем цикл    (99-> 100)
#     total += count # считаем сумму  (+ 99 + 100)
# print("Сумма: ", total, "Шаг: ", count)



# ages = [12,14,18,21,26,33]
# print(ages[0]) # для примера вывода без цикла
# print(ages[1])
# print(ages[2])
# print(ages[3])


# ages = [12,14,18,21,26,33] # Список возрастов
# count = 0 # переменная для шага
# while count < len(ages): # пока count, меньше, чем длина списка
#     if ages[count] < 18: # ages[0] < 18 (12 < 18)
#         print("Нельзя", ages[count])
#     else:
#         print("Можно", ages[count])
#     count +=1 # Для конца цикла


# Принимаем возраст у клиента
# count = 0
# while count < 5: # допустим, что покупателей 5
#     age = int(input("введите возраст: ")) # Спрашиваем у каждого покупателя возраст
#     if age < 18: # Проверка на возраст
#         print("nope")
#     else:
#         print("yup")
#     count += 1 # продолжение/конец цикла




# Пример с выходом из цикла
# count = 0
# while True: # допустим, что покупателей 5
#     age = int(input("введите возраст: (число или 0 для выхода) ")) # Спрашиваем у каждого покупателя возраст
#     if age > 0:
#         if age < 18: # Проверка на возраст
#             print("nope")
#         else:
#             print("yup")
#     else:
#         break # выход из цикла, если покупателю меньше 0



# Программа, для вывода четных чисел
# count = 1
# while count <= 10:
#     if count % 2 == 0:
#         print(count)
#     count += 1


# программа для вывода четных чисел
# count = 0
# while count < 10:
#     print(count)
#     count += 2


# Напишите программу, которая принимает
# 3 фильма, и добавляет их в список (через цикл)
# count = 0
# my_list = [] # переменная для хранения фильмов
# while count < 3: # Условие повторения
#     film = input("введите фильм: ") # спрашивает фильм 3 раза
#     my_list.append(film) # добавляет каждый отдельный фильм
#     count += 1 # продолжение цикла
# print(my_list)



# films = ["Shutter Island", "Avengers", "Titanic", "Beautiful mind", "The  edge of tomorrow"]
# while 0 < len(films):
#     del films[0] # Пример удаления используя циклы
# print(films)

# KAHOOT.IT -> letscode


