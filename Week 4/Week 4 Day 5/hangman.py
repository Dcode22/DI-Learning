import random

gallows1 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
              |\n\
              |\n\
              |\n\
              |\n\
              |\n\
              |\n\
           ------"
gallows2 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
     |        |\n\
     |        |\n\
     |        |\n\
     |        |\n\
              |\n\
              |\n\
           ------"
gallows3 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
     |        |\n\
_____|        |\n\
     |        |\n\
     |        |\n\
              |\n\
              |\n\
           ------"
gallows4 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
     |        |\n\
_____|_____   |\n\
     |        |\n\
     |        |\n\
              |\n\
              |\n\
           ------"
gallows5 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
     |        |\n\
_____|_____   |\n\
     |        |\n\
     |        |\n\
    /         |\n\
   /          |\n\
           ------"
gallows6 = f"     ---------|\n\
     |        |\n\
   ------     |\n\
  |_*__*_|    |\n\
     |        |\n\
_____|_____   |\n\
     |        |\n\
     |        |\n\
    / \       |\n\
   /   \      |\n\
           ------"
gallows_list = [gallows1, gallows2, gallows3, gallows4, gallows5, gallows6]
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
print(word)
secret_word = word
print("guess the word below:")
print("-"*len(secret_word))

def guess(lives_lost):
    player_guess = input("guess a letter: ")
    if player_guess in secret_word:
        print("-"*secret_word.index(player_guess),player_guess, "-"*(len(secret_word)-secret_word.index(player_guess)-1))
        guess(lives_lost)
    else:
        print("incorrect")
        print(gallows_list[lives_lost])
        lives_lost += 1
    guess(lives_lost)


def main():
    lives_lost = 0
    guess(lives_lost)
main()
