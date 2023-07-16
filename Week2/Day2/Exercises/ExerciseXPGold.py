# import random
#
# list_one = [1, 2, 3, 4]
# list_two = [5, 6, 7, 8]
# list_one.extend(list_two)
#
# for i in range(1499, 2501):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)
#
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name = input("What is your name?").capitalize()
# if user_name in names:
#     print(names.index(user_name))
#
# highest = 0
# for i in range(0, 3):
#     number = int(input(f"Insert {i + 1}st number"))
#     if number > highest:
#         highest = number
# print(highest)
#
# # words = []
# # for i in range(0, 8):
# #     word = input("Enter a word:\n")
# #     words.append(word)
# # letter = input("Enter a single character.\n")
# # for i in words:
# #     if letter in i:
# #         print(i.find(letter))
# #     else:
# #         print(f"We didn't find {letter} in {i}")
# numbers_to_mil = []
# for i in range(1, 1000001):
#     numbers_to_mil.append(i)
# print(min(numbers_to_mil), max(numbers_to_mil))
# print(sum(numbers_to_mil))
#
# str_numbers = input("Enter number separated by comma:\n")
# lst_num = str_numbers.split(",")
# lst_num_tup = tuple(lst_num)
# print(lst_num, lst_num_tup)
#
#
import random

flag = True
wins = 0
losses = 0
while flag:
    rand_num = random.randint(1, 9)
    user_number = input("Enter a number between 1-9. press 'q' to quit. ")
    if user_number.lower() == "q":
        print(f"In total of {wins+losses} games played, You won {wins} and lost {losses}.")
        flag = False
    elif int(user_number) == rand_num:
        print("Winner!\n")
        wins += 1
        continue
    else:
        losses += 1
        print(f"The number is: {rand_num}.\nBetter luck next time!\n")
