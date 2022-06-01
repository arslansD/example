# Задача 1
# my_dict = {"films": ["Shutter Island", "Sherlock"],
#            "soundtrack": ["Hans Zimmer"]}
# count = 0
# for key, value in my_dict.items(): # Первый способ с items()
#     print(value)
#     if type(value) == list:
#         count += 1
# print(f"Списков {count}")

# count = 0
# for value in my_dict.values(): # Второй способ с values()
#     if type(value) == list: # если тип данных равен списку,
#         count += 1 # то мы добавляем + 1
# print(f"Списков {count}")





# Задача 2
# numbers = {} # словарь, куда мы добавляем числа
# for element in range(1, 11): # для чисел с 1 до 11
#     numbers[element] = element ** 2 # добавляем ключ-значение
# print(numbers)




# Вторая задача
num = int(input("введите сторону: "))
perimetr = num + num + num + num # Периметр
square = num * num # площадь
print(perimetr, square)

