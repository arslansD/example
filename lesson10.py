# st = input("введите текст: ").lower() # изменяем регистр на маленькие буквы
# subst = input("введите, что вы ищете: ").lower()
# if subst in st: # поиск элемент с помощью оператора in
#     print("Есть контакт!")
# else:
#     print("Мимо!")



# my_str = "hello"
# print(my_str[0])


# text = "Neolabs"
# print(text) # выводит всё содержимое

# #      01234567
# text1 = "Neolabs"
# print(text1[0])
# print(text1[-1])
# print(text1[-8]) # все диапазона, покажет ошибку


# text2 = "Neolabs"
# print(text2[0:3]) # покажет от 0 до 3 элемента (neo)
# print(text2[2:]) # от 2 до конца
# print(text2[:-1]) # от начала до -1 элемента

# text3 = "hello"
# del text3
# print(text3) # выведет ошибку, потому что строки уже нет




# Конкатенация
# word1 = "Добро пожаловать "
# word2 = input("введите имя пользователя: ")
# print(word1 + word2)


# text4 = "hello "
# print(text4 * 3) # Можно умножить строку



# count = 0
# user = input("введите текст: ")
# for letter in user:
#     if letter == "a":
#         count += 1
# print("Букв 'а' найдено", count)



# print('''He said, "what's there?"''')
# print("He said, \"what's there?\"")
# print('He said, "what\'s there?"')






# num1 = int(input("введите число: "))
# num2 = int(input("введите второе число: "))
# print(num1 + num2)



# nums = input("введите числа: ").split()
# print(nums) # 2 3
# print(int(nums[0]) + int(nums[1]))

# numbers = input("введите числа: ").split() # Принимаем числа в строку
# numbers = list(map(int, numbers)) # превращаем все числа в int
# print(numbers)



# song = "синее синее, небо"
# print(song.replace("синее", "белое")) # замена элементов в строке



# Напишите программу, которая принимает строку
# Если строка, больше 10 элементов,
# Выведите первую букву, количество элементов между,
# последнюю букву
# print(len("International")) # I11l
# word5 = input("введите слово: ")
# if len(word5) > 10:
#     print(word5[0]) # первая буква
#     print(len(word5)-2) # количество букв между началом и концом
#     print(word5[-1]) # последняя буква
# else:
#     print("too short")


# word5 = input("введите слово: ")
# if len(word5) > 10:
#     print(word5[0],len(word5)-2, word5[-1], sep = "") # с помощью сепаратора (1 вариант)
#     print(f"{word5[0]}{len(word5)-2}{word5[-1]}") # С помощью формата (2 вариант)
#     print(word5[0]+str(len(word5)-2)+word5[-1]) # С помощью конкатенации (3 вариант)
# else:
#     print("too short")

# Создайте пустой список, и заполните его числами от 1 до 1000
# выведите сумму элементов в списке
# numbers = []
# for num in range(1, 1001):
#     numbers.append(num)
# print(sum(numbers)) # с помощью команды sum

# summary = 0
# for element in numbers: # с помощью цикла for
#     summary += element
# print(summary)


# count = 0
# total = 0
# while count < len(numbers): # с помощью цикла while
#     total += numbers[count]
#     count += 1
# print(total)



#      12345678901
# txt = "hello world"
#        987654321 (со знаком -)
# print(txt[-5:])
# print(txt[5:])
