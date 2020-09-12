import random


class Game:
    def __init__(self):
        self.result_tally = {'win': 0, 'draw': 0, 'loss': 0}

    def get_user_item(self):
        self.user_item = ""
        pot_user_item = input("Pick one of the following moves: \n 'r' for rock \n 'p' for paper\n 's' for scissors\n or enter 'q' to quit game")
        if pot_user_item in ['r', 'p', 's', 'q']:
            self.user_item = pot_user_item

        if self.user_item in ['r', 'p', 's']:
            self.get_computer_item()

    def get_computer_item(self):
        self.computer_item = random.choice(['r', 'p', 's'])

    def get_game_result(self):
        self.game_result = ''
        if self.user_item == self.computer_item:
            self.game_result = 'draw'
        if self.user_item == 'r':
            if self.computer_item == 's':
                self.game_result = 'win'
            if self.computer_item == 'p':
                self.game_result = 'loss'
        if self.user_item == 'p':
            if self.computer_item == 's':
                self.game_result = 'loss'
            if self.computer_item == 'r':
                self.game_result = 'win'
        if self.user_item == 's':
            if self.computer_item == 'r':
                self.game_result = 'loss'
            if self.computer_item == 'p':
                self.game_result = 'win'

        return self.game_result


    def play(self):

        self.get_user_item()
        if self.user_item == 'q':
            print("Game Over!")
            return print(self.result_tally)

        self.get_game_result()

        print(f"You played {self.user_item}, the computer played {self.computer_item}: {self.game_result}!")

        self.result_tally[self.game_result] += 1
        self.play()

