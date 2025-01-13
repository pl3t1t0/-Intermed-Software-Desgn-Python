from dataclasses import dataclass

@dataclass
class Enemy(object):
    health: int = 100
    damage: int = 10
    name: str = "John"
    id: int = 0000

    def __str__(self):
        return f"Enemy: \nname: {self.name}  damage: {self.damage}  health: {self.health}  id: {self.id}"


    # Getters and Setters
    def get_health(self) -> int:
        return self.health
    def set_health(self, newhealth: int):
        assert type(newhealth) == int, "please give set_health an integer value"
        self.health = newhealth
    def get_name(self) -> str:
        return self.name
    def set_name(self, newname: str):
        assert type(newname) == str, "please give set_name a string value"
        self.name = newname
    def get_damage(self) -> int:
        return self.damage
    def set_damage(self, newdamage: int):
        assert type(newdamage) == int, "please give set_damage an integer value"
        self.damage = newdamage

    def apply_damage_to_self(self, damage_taken):
        if damage_taken >= self.health:
            damage_taken = self.health
        self.health -= damage_taken

    def weaken_enemy(self):
        self.damage /= 2

# Main program
def main():
    # Create an object of Enemy class
    enemy = Enemy()

    # Test the default values
    print("Default Enemy:", enemy)

    # Set new health, name, and damage using setters
    enemy.set_health(80)
    enemy.set_name("Drake")
    enemy.set_damage(15)

    # Get the updated values using getters and print them
    print("Updated Enemy Health:", enemy.get_health())
    print("Updated Enemy Name:", enemy.get_name())
    print("Updated Enemy Damage:", enemy.get_damage())

    # Apply damage to the enemy
    enemy.apply_damage_to_self(30)
    print("Enemy after taking damage:", enemy)

    # Weaken the enemy
    enemy.weaken_enemy()
    print("Enemy after being weakened:", enemy)

if __name__ == "__main__":
    main()