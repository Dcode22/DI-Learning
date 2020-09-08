class Palindrome_or_not:
    def __init__(self, word):
        self.word = word
    
    def palindrome(self):
        if self.word == self.word[::-1]:
            return True
        
        else:
            return False

def main():
    pizza = Palindrome_or_not("pizza")

    print(pizza.palindrome())

    racecar = Palindrome_or_not("racecar")

    print(racecar.palindrome())

main()