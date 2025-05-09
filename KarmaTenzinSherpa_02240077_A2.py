#MY_Game:)
import random
from Pokemon_Binder import run_game

class My_user:
    def __init__(self):
        self.score= 0
    
    def update_score(self,points):
        self.score+= points
        print(f"User's new score: {self.score}")

class Game:
    def __init__(self):
        self.score = My_user()
        self.min_number= 1
        self.max_number= 7

    def guess_number(self):
        while True: 
            try:
                guess = int(input(f"Select a number betweeen {self.min_number} and {self.max_number}: "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print("Select a number from given range:)")
            except ValueError:
                print("Sorry,your selected number is not in my range:) Enter a number again:)")

    def play_turn(self):
        print("   Try Again   ")
        target= random.randint(self.min_number, self.max_number)
        guess = self.guess_number()
        
        if guess == target:
            print("Wow not bad player, you got it right, +10 points")
            self.score.update_score(10)
        else:
            print("Not this time,still then try champ. -5")
            self.score.update_score(-5)

    def start_game(self):
        print("Hi there:),you ready for guess game")
        turns=5
        for _ in range(turns):
            self.play_turn()
        print(f"Thank you!!!hope you enjoyed the game. Total score={self.score}")

# __name__ == "__main__":
#    game = Game()
 #   game.start_game()


#MY rock,paper and scissor system
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
            print("Nice try mate,better luck next time")
        else:
            print("Neither you lost nor you won, it's a tie; Good game")

if __name__ == "__main__":
    game = Game()
    game.start_game()






class Question:
    def __init__(self, question_text, choices, correct_answer, category):
        self.question_text = question_text  
        self.choices = choices  
        self.correct_answer = correct_answer  
        self.category = category  

  
    def is_correct(self, answer):
        return answer == self.correct_answer

class TriviaGame:
    def __init__(self):
        self.score = 0  
        self.questions = []  
        self.categories = {}  

    
    def add_question(self, question):
        if question.category not in self.categories:
            self.categories[question.category] = []
        self.categories[question.category].append(question)

    
    def play(self):
        print("Welcome to Trivial game zone!")
        
       
        print("Choose a Category,enjoy the ahead :")
        for index, category in enumerate(self.categories.keys(), 1):
            print(f"{index}. {category}")
        
        category_choice = int(input("Select a category (1-4): "))
        selected_category = list(self.categories.keys())[category_choice - 1]
        
        print(f"You selected {selected_category}!")

       
        questions_in_category = self.categories[selected_category]
        questions_to_ask = questions_in_category[:10]

       
        for index, question in enumerate(questions_to_ask, 1):
            print(f"Question {index}: {question.question_text}")
            for index, choice in enumerate(question.choices, 1):
                print(f"{index}. {choice}")
            
            
            user_answer = int(input("Choose your answer (1-3): "))
            
            
            if question.is_correct(question.choices[user_answer - 1]):
                print("Correct it is:),SMARTYY...")
                self.score += 1
            else:
                print(f"Sadd,you are wrong:(. The correct answer is: {question.correct_answer} ")

            
            print(f"Your current score: {self.score}/{index}")

       
        print(f"\nGame Over! Your final score is {self.score}/{len(questions_to_ask)}.")

q1 = Question("What is the largest island on the world?", ["Greenland", "Australia", "Madagascar", "South America"],"Greenland" ,"Geography")
q2 = Question("What is the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Missippi River"], "Nile River", "Geography")
q3 = Question("What is the symbol of water", ["02", "CH4", "CO2", "H2O"], "H2O", "Science")
q4 = Question("Which conutry has most natural lakes?", ["Philippines", "China", "South Korea", "Canada"], "Canada", "Geography")
q5 = Question("In which year did World War II end?", ["1941", "1943", "1945", "1950"], "1945", "History")
q6 = Question("What is the unit of electrical resistance?", ["Volt", "Ohm", "Ampere", "Watt"], "Ohm", "Science")
q7 = Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter", "Science")
q8 = Question("Who was the first President of the United States?", ["George Washington", "John Adams", "Thomas Jefferson", "Abraham Lincoln"], "George Washington", "History")
q9 = Question("Which country is known as the Land of the Rising Sun?", ["China", "South Korea", "Japan", "India"], "Japan", "Geography")
q10 = Question("What is the boiling point of water?", ["90°C", "100°C", "110°C", "120°C"], "100°C", "Science")
q11 = Question("Who was the leader of Nazi Germany during World War II?", ["", "Pablo Picasso", "Adolf Hitler", "Joseph Stalin"], "Adolf Hitler", "History")
q12 = Question("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Southern", "PaciBenito Mussolinific"], "Pacific", "Geography")


game = TriviaGame()
game.add_question(q1)
game.add_question(q2)
game.add_question(q3)
game.add_question(q4)
game.add_question(q5)
game.add_question(q6)
game.add_question(q7)
game.add_question(q8)
game.add_question(q9)
game.add_question(q10)
game.play()


def main_menu():
    while True:
        print("------Main Menu------")
        print("1. My Guessing Number Game")
        print("2. Rock, Paper and Scissors Game")
        print("3. My Trivia Quiz Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Exit The Program")
        choice = input("Select a mode (1-6): ").strip()


if __name__ == "__main__":
    main()