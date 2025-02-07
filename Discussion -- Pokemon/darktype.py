from random import random
from pokemon import Pokemon

# Placeholder classes to avoid undefined references
class GhostType(Pokemon): pass
class PsychicType(Pokemon): pass
class FightingType(Pokemon): pass
class FairyType(Pokemon): pass
class DarkType(Pokemon):

    def __init__(self, name, trainer, hp=None):
        super().__init__(name, trainer)
        self.basic_attack = "Fling"
        self.prob = 1.0 # 100% chance of pobability
        if hp is not None:
            self.hp = hp

    def __str__(self):
        return f"Pokemon name: {self.name}\tTrainer: {self.trainer}\n"\
               f"Level: {self.level}\tHP: {self.hp}"

    def attack(self, other):
        # Set base damage
        damage = Pokemon.damage

        # Adjust damage based on strengths and weaknesses
        if isinstance(other, (GhostType, PsychicType)):
            damage *= 2  # Strong against Ghost and Psychic
        elif isinstance(other, (FightingType, DarkType, FairyType)):
            damage /= 2  # Weak against Fighting, Dark, and Fairy

        # Apply attack
        super().attack(other)

        # Inflict paralysis if probability condition is met
        if random() < self.prob:
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")

        # Reset damage to original
        self.damage = Pokemon.damage
