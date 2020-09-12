from game import Game


def get_user_menu_choice():
    print("Welcome to ROCK-PAPER-SCISSORS!\nMenu:\n g = start new game\n q = quit game and display results")
    user_menu_choice = input("Enter a menu item: ")
    if user_menu_choice == "g":
        user_game = Game()
        user_game.play()
    elif user_menu_choice == "q":
        print("Game Aborted")

    else:
        print("Invalid menu choice: Try again!")
        get_user_menu_choice()


def main():
    get_user_menu_choice()
    game_results = {}


main()
