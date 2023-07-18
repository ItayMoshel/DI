def sort_words(s):
    words = s.split(",")
    words = [word.strip() for word in words]
    sorted_words = sorted(words)
    result = ",".join(sorted_words)
    return result


input_string = input("Enter comma-separated words: ")

sorted_sequence = sort_words(input_string)
print(sorted_sequence)


def longest_word(sentence):
    sentence = sentence.strip()
    words = sentence.split()
    longest = ""
    longest_length = 0

    for word in words:
        word_length = len(word)

        if word_length > longest_length:
            longest = word
            longest_length = word_length

    return longest


sentence1 = "Margaret's toy is a pretty doll."
print(longest_word(sentence1))

sentence2 = "A thing of beauty is a joy forever."
print(longest_word(sentence2))

sentence3 = "Forgetfulness is by all means powerless!"
print(longest_word(sentence3))
