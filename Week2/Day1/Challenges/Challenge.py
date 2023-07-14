import random

user_string = input("Input a string with 10 characters")
string_length = len(user_string)

if string_length > 10:
    print("string too long")
elif string_length < 10:
    print("string not long enough")
else:
    print("perfect string")
    print(f"first letter is string: {user_string[0]}, last letter in string: {user_string[-1]}")
    constructed_string = []
    for i in user_string:
        constructed_string.append(i)
        print("".join(constructed_string))
    random.shuffle(constructed_string)
    print("".join(constructed_string))

