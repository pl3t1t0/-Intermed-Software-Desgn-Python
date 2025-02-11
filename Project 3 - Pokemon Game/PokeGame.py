from random import choice
from pokemon import Pokemon
from darktype import DarkType
from ice_pokemon import IceType

# Lapras class by Chungmeng Cheong

class PokeGame:
    def __init__(self):
        self.game_master = []
        self.setup()
    
    def setup(self):
        """Create seven instances of any combination of Pokemon, DarkType, and IceType."""
        self.game_master.append(Pokemon("Pikachu", "Ash"))
        self.game_master.append(Pokemon("Charizard", "Red"))
        self.game_master.append(DarkType("Umbreon", "Gary"))
        self.game_master.append(DarkType("Zoroark", "Jessie"))
        self.game_master.append(IceType("Glaceon", "Misty"))
        self.game_master.append(IceType("Lapras", "Brock"))
        self.game_master.append(Pokemon("Bulbasaur", "Oak"))
    
    def drawPokemon(self):
        """Pull an instance from the list of Pokemon, display it, and return the instance."""
        if not self.game_master:
            print("Game Over")
            return None
        selected_pokemon = self.game_master.pop()
        if selected_pokemon.hp is None:
            selected_pokemon.hp = 50  # Assign a default HP if missing
        print(f"\nOpponent Pokémon: {selected_pokemon.name}, Trainer: {selected_pokemon.trainer}, HP: {selected_pokemon.hp}")
        return selected_pokemon

def main():
    game = PokeGame()
    while True:
        opponent = game.drawPokemon()
        if opponent is None:
            break
        print("Select a Pokemon type to battle:")
        print("1. Normal\n2. Dark\n3. Ice")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice in ["1", "2", "3"]:
                break
            print("Invalid choice, please enter a number between 1 and 3.")
        
        while True:
            name = input("Enter your Pokemon's name: ")
            if name.lower() in ["pokemon", "darktype", "icetype"]:
                print("Invalid name. Please choose a different name.")
            else:
                break
        
        while True:
            try:
                hp = int(input("Enter your Pokemon's HP (positive integer): "))
                if hp > 0:
                    break
                else:
                    print("HP must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for HP.")
        
        if choice == "1":
            player_pokemon = Pokemon(name, "Player")
            player_pokemon.hp = hp  # Manually assign HP
        elif choice == "2":
            player_pokemon = DarkType(name, "Player", hp)
        elif choice == "3":
            player_pokemon = IceType(name, "Player", hp)
        
        print(f"\n{player_pokemon.name} is attacking {opponent.name}!")
        player_pokemon.attack(opponent)
        print(f"{opponent.name}'s HP after attack: {opponent.hp}\n")

if __name__ == "__main__":
    main()
