from anagram_checker import AnagramChecker


def get_user_input():
    return input("Enter a word (or type 'exit' to quit): ").strip()


def display_results(word, is_valid, anagrams):
    print("\nYOUR WORD: '{}'".format(word))
    if is_valid:
        print("This is a valid English word.")
    else:
        print("This is NOT a valid English word.")
    if anagrams:
        print("Anagrams for your word:", ", ".join(anagrams))
    else:
        print("No anagrams found for your word.")


def main():
    word_list_file = "wordlist.txt"
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if ' ' in user_input:
            print("Error: Only a single word is allowed.")
            continue

        if not user_input.isalpha():
            print("Error: Only alphabetic characters are allowed.")
            continue

        word = user_input.lower()

        is_valid_word = anagram_checker.is_valid_word(word)
        anagrams = anagram_checker.get_anagrams(word)

        display_results(word, is_valid_word, anagrams)


if __name__ == "__main__":
    main()
