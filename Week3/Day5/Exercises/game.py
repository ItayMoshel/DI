import random


class Game:
    def get_user_item(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                return user_choice

    def get_computer_item(self):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == 'rock' and computer_item == 'scissors') or \
                (user_item == 'paper' and computer_item == 'rock') or \
                (user_item == 'scissors' and computer_item == 'paper'):
            return "win"
        else:
            return "loss"

    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)

        print(f"You selected {user_choice}. The computer selected {computer_choice}.")
        if result == "win":
            print("You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")

        return result
