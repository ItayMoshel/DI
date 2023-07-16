import math
import random

C = 50
H = 30
numbers = input("Enter a set of comma separated numbers")

for i in numbers.split(","):
    D = int(i)
    Q = round(math.sqrt((2 * C * D) / H))
    if i == numbers.split(",")[-1]:
        print(Q)
        break
    print(Q, end=",")


def some(listofnums):
    small = 0
    large = 0
    sumofx = 0
    for i in listofnums:
        if i < small:
            small = i
        if i > large:
            large = i
        sumofx += i
    avgofsum = sumofx / len(listofnums)
    print(f"smallest = {small}, largest = {large}, sum = {sumofx}, avg = {avgofsum}")


def somefunc(listofnums):
    print(*listofnums)
    print(sorted(listofnums, reverse=True))
    sum_of_nums = sum(listofnums)
    print(sum_of_nums)
    first_last = [listofnums[0], listofnums[-1]]
    print(first_last)
    bigger_then_50 = [i for i in listofnums if i > 50]
    print(bigger_then_50)
    smaller_then_10 = [i for i in listofnums if i < 10]
    print(smaller_then_10)
    sqrted = [i * i for i in listofnums]
    print(sqrted)
    without_dups = list(dict.fromkeys(listofnums))
    print(without_dups)
    avg = sum_of_nums / len(listofnums)
    print(avg)
    highest_num = max(listofnums)
    print(highest_num)
    smallest_num = min(listofnums)
    print(smallest_num)
    some(listofnums)


lst_of_nums = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

somefunc(lst_of_nums)

lst_of_user_nums = []
for i in range(0, 10):
    user_input = int(input(f"Please enter {10 - i} numbers between -100 and 100. "))
    lst_of_user_nums.append(user_input)

somefunc(lst_of_user_nums)

ten_gen_nums = []
for i in range(0, 10):
    ten_gen_nums.append(random.randint(-100, 100))
print(ten_gen_nums)

somefunc(ten_gen_nums)

some_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
lst_of_words = some_input.split(" ")
for i in list(dict.fromkeys(lst_of_words)):
    print(f"{i}:{lst_of_words.count(i)}")

para = """We believe that we can change the things around us in accordance with our desires we believe it because otherwise we can see no favourable outcome. 
We do not think of the outcome which generally comes to pass and is also favourable we do not succeed in changing things in accordance with our desires, but gradually our 
desires change. 
The situation that we hoped to change because it was intolerable becomes unimportant to us. 
We have failed to surmount the obstacle, as we were absolutely determined to do, but life has taken us round it, led us beyond it, and then if we turn round to gaze into 
the distance of the past, we can barely see it, so imperceptible has it become."""

length = len(para)
words = para.replace("\n", "").replace(":", "").split(" ")
total_words = len(words)
sentence = para.replace("\n", "").split(".")
unique = set(words)
space = para.count(" ")
print(sentence, len(sentence))


def word_count(st):
    counts = dict()
    words_num = st.split()

    for word in words_num:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
