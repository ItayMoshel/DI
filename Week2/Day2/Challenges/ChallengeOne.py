user_num = int(input("Enter a number"))
user_length = int(input("Enter length"))
multiples = []
for i in range(1, user_length + 1):
    multiples.append(user_num * i)
print(multiples)


user_word = input("Enter a word: ")
new_word = ""
prev = ""
for c in user_word:
    if len(new_word) == 0:
        new_word += c
        prev = c
    if c == prev:
        continue
    else:
        new_word += c
        prev = c
print(new_word)