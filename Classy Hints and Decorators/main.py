from dataclasses import dataclass, field

@dataclass
class MyClass:
    ID: int = field(default=0)
    name: str = field(default="Unknown")
    age: int = field(default=0)

    def __str__(self) -> str:
        return f"MyClass(ID: {self.ID}, Name: {self.name}, Age: {self.age})"

    # Getter for ID
    def get_ID(self) -> int:
        return self.ID

    # Setter for ID
    def set_ID(self, ID: int) -> None:
        if ID < 0:
            raise ValueError("ID cannot be negative.")
        self.ID = ID

    # Getter for name
    def get_name(self) -> str:
        return self.name

    # Setter for name
    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.name = name

    # Getter for age
    def get_age(self) -> int:
        return self.age

    # Setter for age
    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = age
