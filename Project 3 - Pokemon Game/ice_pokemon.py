# Pikachu class by Chungmeng Cheong
"""Define Ice type Pokemon for CS3B mandatory discussion."""

from pokemon import Pokemon
from random import random

# main class defined by this module
class IceType(Pokemon):
    """Create an Ice Pokemon class inherited from base Pokemon class."""
    basic_attack = "Freeze Shock"
    prob = 0.3

    def __init__(self, name:str, trainer:str, hp=None):
        """Initialize pokemon with custom HP."""
        super().__init__(name, trainer)
        if hp is None:
            self.hp = hp

    def __str__(self):
        """Facilitate printing of an overview the Pokemon."""
        formatted_string = (f"Pokemon name: {self.name}\t Trainer: {self.trainer}\n"
                      f"Level: {self.level}\t HP: {self.hp}\n"
                      f"Basic attack: {self.basic_attack}\t Probability to paralyze: {self.prob}")
        return formatted_string

    def attack(self, other):
        """Inflict damage and paralysis on other Pokemon based on modifiers."""
        if isinstance(other, (FlyingType, GrassType, DragonType)):
            self.damage = Pokemon.damage * 2  # Increase damage against pokemon types that Ice types are strong against.
        elif isinstance(other, (FireType, WaterType, IceType)):
            self.damage = Pokemon.damage / 2  # Decrease damage against pokemon types that Ice types are weak against.
        else:
            self.damage = Pokemon.damage  # Else normal damage.
        super().attack(other)
        # Inflict special status on enemy, probabilistically.
        if random() < self.prob and type(other) != IceType:
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")


# placeholder classes for pokemons that Ice type is strong or weak against
class FlyingType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class GrassType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class DragonType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class FireType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class WaterType(Pokemon):
    """Create placeholder types of pokemon."""
    pass


# # main program to test cases
# def main():
#     """Test behaviour of Pokemon classes."""
#     glaceon = IceType("Glaceon", "Ash", 62)
#     print(glaceon, "\n")
#
#     mew = Pokemon("Mew", "Lance")
#     print("***Glaceon attacks Mew, a basic type")
#     glaceon.attack(mew)
#     print(f"Mew's hp: {mew.hp}\n")
#
#     flareon = FireType("Flareon", "Lance")
#     print("***Glaceon attacks Flareon, a type weak against")
#     glaceon.attack(flareon)
#     print(f"Flareon's hp: {flareon.hp}\n")
#
#
# if __name__ == "__main__":
#     main()