
MAX_POKEDEX_NUMBER = 1025 # Highest Pokemon number
CARDS_PER_PAGE = 64 # Cards in each page
GRID_SIZE = 8 # Size of page


class PokemonCard:
    def __init__(self, pokedex_number):
        self.pokedex_number = pokedex_number
        # Calculate page based on card position
        self.page_number = (pokedex_number - 1) // CARDS_PER_PAGE + 1
        pos = (pokedex_number - 1) % CARDS_PER_PAGE
        self.row = pos // GRID_SIZE + 1  # 1-based row
        self.col = pos % GRID_SIZE + 1   # 1-based column

    def get_position(self):
        return f"Page: {self.page_number}\nPosition: Column {self.col}, Row {self.row}" # Position of dex 


class Binder:
    def __init__(self):
        # In-memory storage: set for fast duplicate check, dict for card data
        self.cards_set = set()  # Stores Pokédex numbers for O(1) lookup
        self.cards_dict = {}    # Maps Pokédex numbers to PokemonCard objects

    def add_card(self, pokedex_number):
        # Validate number
        if not (1 <= pokedex_number <= MAX_POKEDEX_NUMBER):
            return "Invalid Pokédex number. Must be between 1 and 1025."

        # Check for duplicates
        if pokedex_number in self.cards_set:
            card = self.cards_dict[pokedex_number]
            return (f"{card.get_position()}\n"
                    f"Status: Pokédex #{pokedex_number} already exists in the binder.")

        # Add card
        card = PokemonCard(pokedex_number)
        self.cards_set.add(pokedex_number)
        self.cards_dict[pokedex_number] = card
        return (f"{card.get_position()}\n"
                f"Status: Added Pokédex #{pokedex_number}")

    def view_binder(self):
        if not self.cards_set:
            return "Binder is empty."

        sorted_cards = sorted(self.cards_dict.items())
        result = ["\n--- Current Binder ---"]
        for num, card in sorted_cards:
            result.append(f"#{num:03} - Page {card.page_number}, Position (Col {card.col}, Row {card.row})")
        result.append(f"\nTotal cards: {len(self.cards_set)}") #  Total cards collected 
        percent = (len(self.cards_set) / MAX_POKEDEX_NUMBER) * 100
        result.append(f"Completion: {percent:.2f}%")

        if len(self.cards_set) == MAX_POKEDEX_NUMBER: # All cards collected
            result.append("You have caught them all!")

        return "\n".join(result)

    def reset_binder(self):
        # Clears all session memory
        self.cards_set.clear() # Clear card tracking set
        self.cards_dict.clear() # Clear card data mapping
        return "Binder has been reset. All data cleared."

    def get_score(self):
        return len(self.cards_set)  # Return number of unique cards collected


def main():
    binder = Binder() # Initialize a new binder

    while True:
        print("\n--- Pokemon Binder Manager ---")
        print("1. Add Pokemon Card")
        print("2. Reset binder / Exit menu")
        print("3. View Pokedex Status")
        print("4. Exit program")
        choice = input("Select a mode (1-4): ").strip()

        if choice == '1':
            try:
                number = int(input("Enter Pokédex number (1-1025): "))
                result = binder.add_card(number)
                print(result)
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 1025.")

        elif choice == '2':
            print("Warning: This will erase all data in the current session.")
            action = input("Type 'CONFIRM' to reset or 'EXIT' to return: ").strip().upper()
            if action == "CONFIRM":
                print(binder.reset_binder())
            elif action == "EXIT":
                print("Returning to main menu...")
            else:
                print("Invalid input.")

        elif choice == '3':
            print(binder.view_binder())

        elif choice == '4':
            print(f"\nFinal Score: {binder.get_score()} cards collected.")
            print("Session ended. Gotta catch 'em all!")
            break

        else:
            print("Invalid choice. Please select a valid mode.")

def run_game():
    pokegame = main()
    pokegame.run_game()



if __name__ == "__main__":
    run_game()
