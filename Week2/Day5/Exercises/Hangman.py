import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)
guessed_letters = []


def initialize_game():
    global word
    global guessed_letters
    print("Hangman Game")
    print("Guess the word:")
    print(display_word())
    print()


def display_word():
    global word
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter + " "
        else:
            display += "* "
    return display


def check_guess(letter):
    global word
    if letter.lower() in word:
        guessed_letters.append(letter.lower())
        return True
    else:
        guessed_letters.append(letter.lower())
        return False


def check_win():
    global word
    for letter in word:
        if letter.lower() not in guessed_letters:
            return False
    return True


def play_game():
    initialize_game()
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Enter a single letter.")
            continue

        if check_guess(guess):
            print("Correct guess!")
            print(display_word())
            print()

            if check_win():
                print("Congratulations! You guessed the word correctly.")
                return

        else:
            attempts += 1
            print("Wrong guess!")
            print("Attempts left:", max_attempts - attempts)

    print("You lost! The word was:", word)


play_game()
