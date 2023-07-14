# True, True, False, False, True, False, x = True, y = False, a = 5, b = 10

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))

flag = True

while flag:
    user_input = input("Input your longest sentence without the letter \"A\".\n")
    if "a" in user_input.lower():
        answer = input("The letter \"A\" found in your text, would you like to keep trying? y/n.\n").lower()
        if answer == "n":
            flag = False
        else:
            continue
    else:
        print(f"Congratulations! Your sentence is {len(user_input)} character long!")
        answer = input("Would you like to go at it again? y/n.\n").lower()
        if answer == "n":
            flag = False
        else:
            continue


