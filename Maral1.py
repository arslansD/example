# # Задача A - Последовательность с цифрами
# for element in range(int(input("введите числа: "))):
#     num1, num2 = map(int, input().split())
#
#     for elem in range(num2 - 1):
#         min_num = min(str(num1))
#
#         if (min_num == '0'):
#             break
#
#         max_num = max(str(num1))
#         num1 = num1 + int(min_num) * int(max_num)
#     print(num1)




# Хлоя и последовательность
# num1, num2=map(int, input().split())
# if num2%2!=0:
#     print(1)
# else:
#     total=1
#     while num2%2==0:
#         num2=num2//2
#         total=total+1
#     print(total)



# Счасливое деление
# num =int(input())
# if any(num%i==0 for i in [4,7,47,74,477,474,747,744]):
#   print("YES")
# else:
#     print("NO")


# Арбуз
# num = int(input())
# if num % 2 == 0 and num != 2:
#     print("YES")
# else:
#     print("NO")


# Математика спешит на помощь
# nums = list(map(int, input().split("+")))
# nums.sort()
# if len(nums) > 1:
#     print(*nums, sep="+", end="")
# else:
#     print(*nums)


# Халк
# feelings=(['I hate', 'I love']*50)
# print(*feelings[:int(input())], sep=' that ', end=' it')




# Неправильное вычитание
# nums = list(map(int, input().split()))
# initial = list(str(nums[0]))
# initial = list(map(int, initial))
# operations = nums[1]
# for element in range(operations):
#     if initial[-1] > 0:
#         initial[-1] -= 1
#     else:
#         initial.pop()
# print(*initial, sep="")



# Магниты
# nums = int(input())
# magnets = []
# islands = 1
# for element in range(nums):
#     magnets.append(input())
# for elem in range(len(magnets)-1):
#     if magnets[elem] != magnets[elem+1]:
#         islands += 1
# print(islands)




# Ваня и забор
# nums = list(map(int, input().split()))
# length = nums[1]
# friends = list(map(int, input().split()))
# width = 0
# for element in friends:
#     if element > length:
#         width += 2
#     else:
#         width += 1
# print(width)



# Я люблю AAAB
# user = int(input())
# for element in range(user):
#     text = input()
#     length = len(text)
#     if text[-1] == 'A':
#         print('NO')
#         continue
#     while True:
#         if 'AB' in text:
#             text = text.replace('AB', '')
#         else:
#             break
#     if 'B' not in text and length > 1:
#         print('YES')
#     else:
#         print('NO')


# Злые школьники
# user=int(input())
# for element in range(user):
#     nums=int(input())
#     students=input()
#     total=0
#     while True:
#         if "AP" in students:
#             students=students.replace("AP","AA")
#             total+=1
#         else:
#             break
#     print(total)
