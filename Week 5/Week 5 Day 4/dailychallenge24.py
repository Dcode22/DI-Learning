with open('OneDrive\Desktop\DI-Learning\Week 5\Week 5 Day 4\my_text.txt', 'r') as f:
        text = f.read() 

text = text.split()


class Text:
    def __init__(self, string):
        self.text = string


    def word_frequency(self, word):
        self.text_list = self.text.split()
        self.frequency_count = 0
        for item in self.text_list:
            if item == word:
                self.frequency_count += 1

        return f"The word {word} is found {self.frequency_count} times in the text."
    def unique_words(self):
        
        self.unique_word_list = []
        for i in self.text_list:
            if i not in self.unique_word_list:
                self.unique_word_list.append(i)

        return self.unique_word_list
    
    def word_frequency1(self, word):
        self.text_list = self.text.split()
        self.frequency_count1 = 0
        for item in self.text_list:
            if item == word:
                self.frequency_count1 += 1

        return self.frequency_count1


    def common_word(self):
        self.most_common_word = "none"
        for i in range(len(self.unique_word_list)-1):
            if self.word_frequency1(self.unique_word_list[i+1]) < self.word_frequency1(self.unique_word_list[i]):
                self.most_common_word = self.unique_word_list[i]
        return self.most_common_word



    
    # def from_file(self, file):

def main():
    test = Text("one two two three three three four four four four five five five five five six six six six six six seven seven seven seven seven seven seven eight eight eight eight eight eight eight eight")
    print(test.word_frequency("and"))
    print(test.unique_words())
    print(test.common_word())

main()




