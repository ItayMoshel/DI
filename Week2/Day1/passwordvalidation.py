s_c = "!@#$%^&*()_+=`~?/,.<>[]{}-"
lower, upper, special, digits = 0, 0, 0, 0
password = "R@m@_f0rtu9e$"

if len(password) >= 8:
    for i in password:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
        if i.isdigit():
            digits += 1
        if i in s_c:
            special += 1

if lower >= 1 and upper >= 1 and special >= 1 and digits >= 1 and lower + digits + upper + special == len(password):
    print("Valid Password")
else:
    print("Invalid Password")
