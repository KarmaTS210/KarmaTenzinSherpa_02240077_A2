import random

class My_user:
    def __init__(self):
        self.wins = 0
        self.score = 0  # Added score

    def update_score(self, points):
        self.score += points
        print(f"User's score: {self.score}")

    def update_wins(self):
        self.wins += 1

class Game:
    def __init__(self):
        self.user = My_user()
        self.computer = My_user()
        self.choices = ["rock", "paper", "scissors"]

    def get_user_choice(self):  # Renamed from user_choice
        while True:
            choice = input("Choose rock, paper or scissors: ").strip().lower()
            if choice in self.choices:
                return choice
            else:
                print("Your option is not valid:). Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print(f"Both chose {user_choice}. It's a tie!")
            return "tie"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print(f"{user_choice.capitalize()} beats {computer_choice}! You win this round.")
            return "user"
        else:
            print(f"{computer_choice.capitalize()} beats {user_choice}! Computer wins this round.")
            return "computer"

    def play_turn(self, round_num):
        print(f"---{round_num} ---")
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = self.decide_winner(user_choice, computer_choice)

        if winner == "user":
            self.user.update_score(10)
            self.user.update_wins()
            self.computer.update_score(-5)
        elif winner == "computer":
            self.computer.update_score(10)
            self.computer.update_wins()
            self.user.update_score(-5)
        else:
            print("No points for a tie.")

    def start_game(self):
        print("Greetings, Welcome to Rock, Paper, Scissors!")
        rounds = 5
        for round_num in range(1, rounds + 1):
            self.play_turn(round_num)

        print("\nGame Over!")
        print(f"Your final score: {self.user.score}")
        print(f"Computer's final score: {self.computer.score}")
        print(f"You won {self.user.wins} round(s).")
        print(f"Computer won {self.computer.wins} round(s).")

        if self.user.wins > self.computer.wins:
            print("WOW GREAT, YOU ARE THE CHAMP :)")
        elif self.user.wins < self.computer.wins:
            print("Nice try mate, better luck next time")
        else:
            print("Neither you lost nor you won, it's a tie; Good game")

if __name__ == "__main__":
    game = Game()
    game.start_game()
