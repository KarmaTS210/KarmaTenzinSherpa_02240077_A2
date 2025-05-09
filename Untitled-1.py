import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0  # To track number of rounds won

    def update_score(self, points):
        self.score += points
        print(f"{self.name}'s score is now: {self.score}")

    def update_wins(self):
        self.wins += 1

class Game:
    def __init__(self):
        self.min_number = 1
        self.max_number = 10
        self.user = Player("You")
        self.computer = Player("Computer")

    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"Choose a number between {self.min_number} and {self.max_number}: "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print("Pick a number from the correct range.")
            except ValueError:
                print("That's not a valid number!")

    def play_turn(self, round_num):
        print(f"\n--- Round {round_num} ---")
        target = random.randint(self.min_number, self.max_number)

        user_guess = self.get_user_guess()
        computer_guess = random.randint(self.min_number, self.max_number)
        print(f"Computer guessed: {computer_guess}")

        user_correct = (user_guess == target)
        computer_correct = (computer_guess == target)

        # Score logic
        if user_correct:
            print("✅ You guessed it right! +10 points.")
            self.user.update_score(10)
        else:
            print(f"❌ You missed! The correct number was {target}. -5 points.")
            self.user.update_score(-5)

        if computer_correct:
            print("🤖 Computer guessed it right! +10 points.")
            self.computer.update_score(10)
        else:
            print("❌ Computer missed! -5 points.")
            self.computer.update_score(-5)

        # Win tracking
        if user_correct and not computer_correct:
            self.user.update_wins()
        elif computer_correct and not user_correct:
            self.computer.update_wins()
        # if both are correct or both are wrong = no win awarded

    def start_game(self):
        print("🎮 Welcome to the Guessing Game: You vs Computer!")
        rounds = 10
        for round_num in range(1, rounds + 1):
            self.play_turn(round_num)

        # Final result
        print("\n🏁 Game Over!")
        print(f"Your final score: {self.user.score}")
        print(f"Computer's final score: {self.computer.score}")
        print(f"\n🏆 You won {self.user.wins} round(s).")
        print(f"💻 Computer won {self.computer.wins} round(s).")

        # Decide the winner
        if self.user.wins > self.computer.wins:
            print("🎉 You win the game by winning more rounds!")
        elif self.user.wins < self.computer.wins:
            print("💻 Computer wins the game by winning more rounds!")
        else:
            print("🤝 It's a tie in number of wins!")

# Start the game
if __name__ == "__main__":
    game = Game()
    game.start_game()
