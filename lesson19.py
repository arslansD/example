# Задача 1 Практического теста
# num = int(input("введите число: "))
# check = "Ne prostoe" # Пока что число простое
# for i in range(2, num): # 9/2 - 9/3
#     if num % i == 0: # 11/2 11/3 11/4 11/5 11/6 11/7 11/8 11/9 11/10
#                     # 6/2 = 3
#         print("Нет, это не простое число")
#         check = 'prostoe'
#         break
#     print("пока не нашли", i)
# if check == "Ne prostoe":
#     print("Да, это простое число")




# Задача 1 Практического теста, вариант 2
# num = int(input("введите число: "))
# exception = (1,2,3,5)
# if num in exception:
#     print("простое")
# elif num%2!=0 and num%3!=0 and num%5!=0:
#     print("простое")
# else:
#     print("не простое")



# Задача 2
# num = int(input("введите число: "))
# perimeter = num * 4
# square = num * num
# print(perimeter, square)


# Задача 3
# sample = {"Physics": 99,
#           "Math": 62,
#           "Python": 93}
# print(min(sample.values())) # Вывести минимальное значение списка



# Задача 4
# exception = [list, tuple, dict]
# tuple1 = ("Tuple", [10,20,30], (40,50,70))
# for element in tuple1:
#     if element == 20:
#         print(element)
#     elif (type(element) in exception) and (20 in element):
#         print(20)


# my_list = []
# for element in range(5):
#     my_list.append("*") # добавляем звездочку
#     print(*my_list) # сразу выводим


# Задача 6
# for element in range(-10, 0):
#     print(element)



# Задача 7
# num = int(input("введите число: "))
# if num == 7:
#     print("Lucky")
# elif num == 13:
#     print("cursed")
# else:
#     print("pass")



# Задача 8
# my_list = [1,2,3,4,5,6,7,8,9,10]
# summary = 0
# for element in my_list: # проходимся по списку
#     summary += element # добавляем к переменной каждое число
# print(summary)


# Задача 9
# list1 = ["Alex", "Chyngyz", "Nazira", "Adil", "Elina", "Kanat", "Ali", "Vika"]
# for name in list1:
#     if len(name) > 4: # проверить длину имени
#         print(name)




# Задание 10
# my_dict = {"subject": "Python",
#            "hobbies": ["sleep", "eat"],
#            "playlist": ["In the end", "Car Radio", "I want to break free"],
#            "chocolate": ["Snickers", "Mercy", "Twix", "Milka"]}


# Задача 11
# list1 = [1, 2, 4, 6, 7, 8, 9, 10]
# list2 = [0, 3, 5, 6, 11, 8, 12, 10]
# for element in list1: # пройдемся по числам в списке 1
#     if element in list2: # проверим, есть ли они в списке 2
#         print(element)



def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

def multi(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1/num2)

def power(num1, num2):
    print(num1 ** num2)

def ost(num1, num2):
    print(num1 % num2)


def calculate():
    num1 = float(input("введите первое число: ")) # чтобы принимать вещественные числа тоже
    num2 = float(input("введите второе число: "))
    operations = ["plus", "minus", "multi", "div", "ost", "power"] # допустимые операции
    oper = input("введите команду: ")
    while oper not in operations: # если действие невозможно, то ввод еще раз
        oper = input("введите другую команду: ")

    if oper == "plus":
        add(num1, num2)
    elif oper == "minus":
        sub(num1, num2)
    elif oper == "multi":
        multi(num1, num2)
    elif oper == "div":
        div(num1, num2)
    elif oper == "ost":
        ost(num1, num2)
    elif oper == "power":
        power(num1, num2)

# while True: # цикл калкулятора
#     calculate()
#     again = input("повторить? (yes/no)") # проверка на продолжение
#     if again == "yes":
#         calculate() # повторный запуск при согласии
#     else:
#         break




def season(month): # Создайте похожую функцию, работающую с днями недели
    winter = (1,2,12)
    spring = (3,4,5)
    summer = (6,7,8)
    autumn = (9,10,11)
    if month in winter:
        print("Зима")
    elif month in spring:
        print("весна")
    elif month in summer:
        print("Лето")
    elif month in autumn:
        print("Осень")
    else:
        print("такого месяца нет!")

# season(9) # Пример запуска



def week(day):
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Party day")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("такого дня нет!")

week(4)
