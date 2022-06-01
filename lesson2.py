# text = "qwerty"
# print(text)


# lyrics = '''one thing, I don’t know why,
# it doesn’t even matter how hard I try,
# keep that in mind I designed this rhyme,
# to explain in due time'''
# print(lyrics)

# Способы вывести строку
# print('hey')
# print("hey")
# print("""hey""")
# print('''hey''')

# #       01234
# word = "Hello"
# print(word[3]) # выводит конкретный элемент строки


# word1 = "hello" # несмотря, что там 4 индекса, длина все равно 5. Потому что 0 - тоже элемент
# print(len(word1)) # len - length - длина


# word2 = "!#!@#@$%$^&*(*_<?<:   12312123  "
# print(len(word2)) # Все что внутри кавычек, считается частью строки


# num = "123445634563453"
# print(type(num)) # выводит тип данных
# print(len(num)) # У числа нельзя узнать длину, поэтому переводим в строку


# num1 = 12345
# num1 = str(num1)
# print(num1[1]) # У числа также, нельзя подобрать индекс, поэтому переводим в строку



# id = "321"
# id = float(id) # Переводит текст в вещественную переменную
# print(id)


# to_do = [1,2,3] # список с числами с 1 до 3
# print(to_do[0]) # выводит элемент на индексе 0
# print(len(to_do)) # выводит длину списка


# my_tuple = (1,2,3)
# print(my_tuple[0]) # через кортеж можно пройтись, и узнать индекс
# print(len(my_tuple)) # показывает длину кортежа


# разница в id списка и кортежа
# my_list = []
# my_list1 = []
# my_tuple = ()
# my_tuple1 = ()
# print(id(my_list)) # списки имеют разный id
# print(id(my_list1))
# print(id(my_tuple)) # кортежи имеют одинаковый id
# print(id(my_tuple1))





# my_list1 = ["поужинать", "посмотреть сериал", "сделать домашку"]
# print(len(my_list1)) # количество задач на сегодня
# print(my_list1[0]) # показывает задачу по индексу

# del my_list1[1] # удалили элемент по индексу
# print(my_list1) # вывели что осталось
# my_list1.append("спать") # append - добавляет элементы в конец списка
# print(my_list1) # выводим что получилось

# Чтобы поставить комментарии, Ctrl + /


# my_list1 = ["поужинать", "посмотреть сериал", "сделать домашку"]
# my_list1[2] = "сидеть в инете до 4 утра" # переприсваивание
# print(my_list1)
# delo = my_list1.pop(0) # pop вытаскивает и сохраняет элемент по индексу
# print(delo) # можно вывести переменную


color_list = ["Red", "Green", "White", "Black"]
# # выведите первый и последний элемент данного списка
# # через индекс+принт, либо через pop
# print(color_list[0])
# print(color_list[3])
# print(color_list.pop(0)) # поп вытаскивает из списка
# print(color_list.pop(2)) # поэтому здесь индекс 2, а не 3



color_list = ["Red", "Green", "White", "Black"]
# Удалите 1 цвет, и добавьте новый цвет
# del или pop для удаления, и append для добавления
# либо поменять значение на прямую
# color_list[1] = "purple" # переприсвоили значение
# print(color_list)
# del color_list[0] # удалили элемент на индексе 0
# color_list.append("yellow") # добавили новый цвет в конец
# print(color_list)
