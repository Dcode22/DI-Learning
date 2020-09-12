from anagramchecker import AnagramChecker


def start():
    user_choice = input("Press 'c' to get all anagrams of a word, or press 'q' to quit:")
    if user_choice == 'q':
        return
    elif user_choice == 'c':
        user_word = input("Enter a word in uppercase: ")
        if user_word.isalpha():
            useword = AnagramChecker()
            if useword.is_valid_word(user_word):
                print(f"Your word: '{user_word}' is a valid English word. \n Anagrams of your word are: {useword.get_anagrams_word(user_word)}")
                start()
        else:
            print("invalid entry, try again!")

            start()

    else:
        print("invalid entry, try again!")

        start()





def main():
    print("working")
    start()

main()