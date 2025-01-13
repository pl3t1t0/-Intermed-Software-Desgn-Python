from dataclasses import dataclass, field

@dataclass
class Wine:
    """
    A class representing a wine with a unique ID and name.
    """
    ID: int = field(default=0)
    name: str = field(default="Unnamed Wine")
    age: int = field(default=0)

    def __str__(self) -> str:
        """
        Magic method to return a string representation of the object.
        """
        return f"Wine[ID = {self.ID}, name = '{self.name}', age = {self.age}]"

    # Getter and Setter for ID
    def get_ID(self) -> int:
        """
        Getter for ID.
        Returns:
            int: The unique ID for the wine.
        """
        return self.ID

    def set_ID(self, new_ID: int) -> None:
        """
        Setter for ID. Ensures the ID is a positive integer.
        Args:
            new_ID (int): The new ID to set.
        """
        if isinstance(new_ID, int) and new_ID > 0:
            self.ID = new_ID
        else:
            raise ValueError("ID must be a positive integer.")

    # Getter and Setter for name
    def get_name(self) -> str:
        """
        Getter for name.
        Returns:
            str: The name of the wine.
        """
        return self.name

    def set_name(self, new_name: str) -> None:
        """
        Setter for name. Ensures the name is a non-empty string.
        Args:
            new_name (str): The new name to set.
        """
        if isinstance(new_name, str) and new_name.strip():
            self.name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter and Setter for age
    def get_age(self) -> int:
        """
        Getter for age.
        Returns:
            int: The age of the wine.
        """
        return self.age

    def set_age(self, new_age: int) -> None:
        """
        Setter for age. Ensures the age is a non-negative integer.
        Args:
            new_age (int): The new age to set.
        """
        if isinstance(new_age, int) and new_age >= 0:
            self.age = new_age
        else:
            raise ValueError("Age must be a non-negative integer.")
