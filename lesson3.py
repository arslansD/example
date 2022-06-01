# ДЗ урока-2
# films = ["Shutter Island", "John Wick", "Fight Club"]
# print(films[0])
# print(films[1])
# print(films[2])
# films.append("Titanic")
# print(films)







# Первый пример использования условия - если
# person = int(input("введите ваш возраст: ")) # 16
# if person >= 18:
#     print("можно")
# elif person < 18:
#     print("Нельзя")




# num1 = int(input("введите первое число: "))
# num2 = int(input("введите второе число: "))
# if num1 > num2: # если num1 больше, чем num2
#     print("Первый победил")
# elif num1 < num2: # НО если вдруг, num1 меньше, чем num2
#     print("Второй победил")
# else: # Если ни одно из вышеуказанных условий не сработало
#     print("Ничья")






# login = "admin" # переменная для хранения логина
# password = "admin123" # переменная для хранения пароля
# user_login = input("введите логин: ") # переменная принимает логин от пользователя, и хранит его
# user_password = input("введите пароль: ")
# # Если оба условия выполнены, работает код под блоком if
# if login == user_login and password == user_password:
#     print("Все работает, вы за-логинены")
# else:
#     print("Нельзя, ошибка логина-пароля!")

# Чтобы отступить код в право нужно нажать: Tab
# Чтобы отступить в обратную сторону: Shift + Tab


# login = "qwerty"
# secret = "yes"
# user1 = input("введите логин: ")
# user_secret = input("введите секрет: ")
# if login == user1 or secret == user_secret: # либо одно, либо другое
#     print("Вы получили привилегии админа")
# else:
#     print("Нет доступа")



# my_set = {1,2,3,4,3,3,3,4,4,4} # сеты удаляют дубликаты
# print(my_set)


month = int(input("введите номер месяца: "))
if month == 1 or month == 2 or month ==12:
    print("зима")
elif month >= 3 and month <= 5:
    print("весна")
elif month >= 6 and month <= 8:         # KAHOOT.IT
    print("Лето")
elif month >=9 and month <=11:
    print("Осень")
else:
    print("Такого месяца нет")
