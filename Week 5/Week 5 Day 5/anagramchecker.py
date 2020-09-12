class AnagramChecker:
    def __init__(self):
        with open('words.txt', 'r') as f:
            self.word_list = f.read()
            self.word_list = self.word_list.split()

    def is_valid_word(self, word):
        if word in self.word_list:
            return True
        else:
            return False

    def get_anagrams_word(self, word):
        word = list(word)
        word = set(word)
        word_anagrams = []
        for i in self.word_list:
            if len(word) == len(i):
                i = list(i)
                if set(i) == word:
                    word_anagrams.append("".join(i))
        return word_anagrams



