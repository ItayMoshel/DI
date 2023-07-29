from game import Game


def get_user_menu_choice():
    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please try again.")


def print_results(results):
    print("Game Results:")
    print(f"Total Wins: {results['win']}")
    print(f"Total Losses: {results['loss']}")
    print(f"Total Draws: {results['draw']}")
    print("Thank you for playing!")


def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()

            if result == 'win':
                results['win'] += 1
            elif result == 'loss':
                results['loss'] += 1
            else:
                results['draw'] += 1

        elif choice == '2':
            print_results(results)

        else:
            print_results(results)
            break


if __name__ == "__main__":
    main()
