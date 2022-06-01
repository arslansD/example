# import lesson22test
# print(lesson22test.add(2123,3123123))



# import math # Ctrl + b
# print("значение pi", math.pi)
# print("Значение e", math.e)





# import math as m # импорт с переименованием
# print("Значение e", m.e)




# from math import pi, e # импортируем определенные функции из модуля
# print(pi, e) # любая другая функция из данного модуля не работает без импорта



# from math import * # Если пользуетесь многими функциями из модуля
# print(e, pi, tau, cos(0.12))



# from math import pi as num # использование всех способ импорта
# print(num)


# Коротко о модулях
# import - импортирует весь модуль, и доступ через оператор .
# from ... import - импортирует определенные функции из этого модуля
# as - переименование


# игра угадай число
# import random
# com = random.randint(1,100) # 1000,000 -> 20
# while True:
#     user = int(input("введите ваше предсказание: "))
#     if com == user:
#         print("вы угадали, число", com)
#         break
#     elif com > user:
#         print("Слишком мало!")
#     else:
#         print("Слишком много!")


# import random
# moves = ["rock", "paper", "scissors"]
# com_win = 0
# user_win = 0
# while com_win != 3 and user_win !=3:
#     com = random.choice(moves)
#     user = input("введите выбор: ")
#     print(f"компьютер выбрал {com}, вы выбрали {user}")
#     if com == "rock" and user == "scissors":
#         com_win += 1
#     elif com == "scissors" and user == "paper":
#         com_win += 1
#     elif com == "paper" and user == "rock":
#         com_win += 1
#
#     elif com == "rock" and user == "paper":
#         user_win += 1
#     elif com == "paper" and user == "scissors":
#         user_win += 1
#     elif com == "scissors" and user == "rock":
#         user_win += 1
#
#     print(f"Ком: {com_win}, пользователь: {user_win}")
#
# if user_win > com_win:
#     print("пользователь победил!")
# else:
#     print("компьютер победил!")




# При импортировании из разных папок, вам нужно указать название папки
# from neolabs_python_day import lesson12practice


