# word = "hello THERE"
# new_word = word.capitalize()
# print("Старая строка:", word)
# print("Новая строка:", new_word)



# text = "Python is Awesome"
# print(text.casefold())
# print(text.lower())



# text1 = "hello there"
# check = text1.count("e") # Посчитать, сколько раз в text1, появляется буква "e"
# print(check)


# #      012345678901
# text2 = "Let it be, let it be, let it be"
# results = text2.find("let it be") # ищет слева-направо, в данном случае 11
# print(results)
# results2 = text2.rfind("let it be") # ищет справа-налево, в данном случае 22
# print(results2)



# sentence = "Python programming is fun"
# print(sentence.index("g")) # команда выводит ПЕРВЫЙ нашедший индекс элемента



# Примеры для работы с форматирование строки
# print("Hello, my name is {}".format("alex"))
# print("Hello, my name is {name}".format(name = "alex"))
# print(f"Hello, my name is {'alex'}")

# text3 = "hello"
# del text3[0] # удалить часть строки НЕЛЬЗЯ


# Добавление строк вместе
# text4 = "hey" + " there" # можно добавить строки
# print(text4)
# print(text4 * 3) # можно умножить строки


# text5 = "hey" - "y" # нельзя отнять от текста
# text6 = "hey"// 3  # нельзя разделить строку


song = """I ponder of something great
My lungs will fill and then deflate
They fill with fire, exhale desire
I know it's dire my time today
I have these thoughts, so often I ought
To replace that slot with what I once bought
'Cause somebody stole my car radio
And now I just sit in silence
Sometimes quiet is violent
I find it hard to hide it
My pride is no longer inside
It's on my sleeve
My skin will scream reminding me of
Who I killed inside my dream
I hate this car that I'm driving
There's no hiding for me
I'm forced to deal with what I feel
There is no distraction to mask what is real
I could pull the steering wheel
I have these thoughts, so often I ought
To replace that slot with what I once bought
'Cause somebody stole my car radio
And now I just sit in silence"""
# song = song.lower()
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for letter in alphabet:
#     check = song.count(letter)
#     print(f"Буква {letter}, появляется в тексте {check} раз(а)")



song1 = """Cause somebody stole my car radio
And now I just sit in silence"""
# song1 = song1.lower()
# ready = [] # список готовых букв
# for letter in song1: # для буквы в маленьком тексте
#     if letter not in ready: # если мы не показывали букву,
#         ready.append(letter) # то тогда мы ее добавляем в список для показа
#
# ready.sort() # сортируем буквы по порядку
# for letter in ready: # для букв в готовом списке
#     results = song1.count(letter) # посчитаем сколько раз появляется в тексте
#     print(f"Буква {letter}, появляется в тексте {results} раз(а)")










# text1 = "außen"
# text2 = "außen"
# text1 = text1.lower() # он оставляет ß как есть
# text2 = text2.casefold() # меняет ß на ss
# if text1 == text2: # "außen" и "aussen"
#     print("da")
# else:
#     print("net")



# сравниваем есть ли элемент внутри списка
# my_list = ["111","222","333"]
# if "3" in my_list:
#     print("da")
# else:
#     print("net")




# my_list2 = ["111","222","333"]
# for text in my_list2:
#     if "3" in text:
#         print("da")
#     else:
#         print("net")


