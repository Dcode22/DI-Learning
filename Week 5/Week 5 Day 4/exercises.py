# exercise1 
import random
with open('OneDrive\Desktop\DI-Learning\Week 5\Week 5 Day 4\sowpods.txt', 'r') as f:
        data = f.read() 
data = data.split()
def get_words_from_file():
    return data
    
def input_length():
    user_length = input("Enter a number between 2 and 20 to get a sentence with that number of words: ")
    try:
        if int(user_length) in range(2,21):
            sent_length = int(user_length)
            return sent_length
        else:
            raise ValueError
    except ValueError:
        print("invalid sentence length")

    
def get_random_sentence(length):
    sentence= []
    for i in range(length):
        sentence.append(random.choice(data))

    final_sentence = ' '.join(sentence) + "."

    final_sentence = final_sentence.lower()




    print(final_sentence)


def main():

    print("This program prints a sentence of random words. The amount of randow words in the sentence is specified by you (the user).")

    sent_length = input_length()
    get_random_sentence(sent_length)
    
    

main()



