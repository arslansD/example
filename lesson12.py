# my_str = "python"
# my_str = list(my_str) # превратили строку в список
# print(my_str)
# print(type(my_str)) # Тип данных


# set = {1,1,1,1,2,2,2}
# set = list(set) # {1,2} -> [1,2]
# print(set)

# my_tuple = (1,2,3)
# my_tuple = list(my_tuple) # поменяли кортеж в список
# print(my_tuple)


# my_dict = {"name":"Alex",
#            "age":123,
#            "hobby":"living"}
# my_dict = list(my_dict)
# print(my_dict) # выдает только ключи (значения исчезают)


# Пример 1
# hey = "Привет"
# hey = list(hey) # Переприсвоили другое значение нашей переменной
# print(hey)
# # Пример 2
# hey = "Привет"
# print(list(hey)) # Выводит в виде списка (только 1 раз)
# print(hey) # При обращении к изначальной переменной, она имеет старое значение



# удаление в списке
# to_do = ["проснуться", "поесть", "пойти на учебу"]
# del to_do[1] # удаление по индексу
# print(to_do)

# удаление и сохранение через команду pop
# to_do = ["проснуться", "поесть", "пойти на учебу"]
# task = to_do.pop() # если без индекса, то выводит последний элемент
# print(task)
# print(to_do)



# to_do = ["проснуться", "поесть", "пойти на учебу"]
# to_do.remove("поесть") # удаляет по названию элемента
# print(to_do)
#
# list1 = [1,2,3]
# list1.clear() # очищает список, но сам список существует
# print(list1)
#
# list2 = [1,2,3]
# del list2 # удаляет переменную полностью и списка уже нет
# print(list2) # покажет ошибку, потому что переменной не существует




# Методы сортировки
# my_list = [4,57,6,9,4,2,5,2,1]
# my_list.sort(reverse=True) # изменяет изначальный список (reversed=True), выводит в обратном порядке
# print(my_list)


# my_list1 = [4,57,6,9,4,2,5,2,1]
# print(sorted(my_list1)) # выводит отсортированный список 1 раз
# print(my_list1) # изначальный список не изменился



# my_list2 = [1,2,3,4,5]
# my_list2.reverse() # сохраняет в обратную сторону
# print(my_list2)


# Копирование через метод copy()
# old_list = [1,2,3]
# new_list = old_list.copy() # копирует список, и является отдельным от старого
# new_list.clear() # изменение нового списка, невлияет на старый
# print(old_list)
# print(new_list)

# Копирование через присваивание
# list1 = [1,2]
# list2 = list1 # Присваивает то же значение
# list2.clear() # При изменении нового списка, старый тоже меняется
# print(list1)
# print(list2)



# my_list = [["Alex"]]
# name = my_list[0] # мы работаем со списком
# print(type(name)) # переменная name, является списком
# print(name[0]) # поэтому, мы можем обратиться по индексу


numbers = [[1,2,3],
           [4,5,6],
           [7,8,9]]
# print(numbers) # выведет элементы в строчку

# for lists in numbers: # для списков внутри двойного списка
#     for num in lists: # для чисел внутри одного списка
#         print(type(num), end = " ") # 1 2 3
#     print()

# Способ полегче для вывода в столбик
# for record in numbers:
#     print(*record) # оператор * выводит список без скобок, запятых, кавычек и т.д



# главное знать, с чем работать, и будет понятно, можно использовать скобки для индекса, или нет
# names = [["Alex"]]
# name_list = names[0] # работаем со списком
# word = name_list[0] # работаем со словом
# print(word[0]) # выводим букву в слове на индексе 0




olymp = [212, 102, 99, 55, 44, 200, 212, 200]
# Выведите победителя серебрянной медали
# то есть второе самое большое число
# olymp.sort()
# print(olymp[-2]) # выводит второе большое число



# nums = input("введите баллы: ").split() # принимаем числа через пробел
# nums = list(map(int, nums)) # Превращаем числа в int
#
# nums = set(nums) # удалили дубликаты с помощью сета
# nums = list(nums) # вернули в список (чтобы работать с командами списка)
#
# nums.remove(max(nums)) # удалили самое большое число
# print(max(nums)) # выдали второе большое число


# Напишите программу, которая
# принимает неизветное количество чисел
# И отнимает их друг от друга
# nums = input().split()
# nums = list(map(int, nums))
# summary = 0
# for element in nums:
#     summary += element # считываем сумму элементов
# print(-summary) # выводим отрицательную сумму (т.к над было отнимать)





# my_list = [1,2,3]
# my_list.insert(0, "hey") # вставляет элемент на индекс
# print(my_list)


