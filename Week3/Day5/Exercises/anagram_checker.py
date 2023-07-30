class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file)

    def is_valid_word(self, word):
        return word.strip().isalpha() and word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w)]
