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
        """ Getter for ID. """
        return self.ID

    def set_ID(self, new_ID: int) -> None:
        """ Setter for ID. Ensures the ID is a positive integer. """
        if isinstance(new_ID, int) and new_ID > 0:
            self.ID = new_ID
        else:
            raise ValueError("ID must be a positive integer.")

    # Getter and Setter for name
    def get_name(self) -> str:
        """ Getter for name. """
        return self.name

    def set_name(self, new_name: str) -> None:
        """ Setter for name. Ensures the name is a non-empty string. """
        if isinstance(new_name, str) and new_name.strip():
            self.name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter and Setter for age
    def get_age(self) -> int:
        """ Getter for age. """
        return self.age

    def set_age(self, new_age: int) -> None:
        """ Setter for age. Ensures the age is a non-negative integer. """
        if isinstance(new_age, int) and new_age >= 0:
            self.age = new_age
        else:
            raise ValueError("Age must be a non-negative integer.")


@dataclass
class Pizza:
    """
    Class about pizza, including info about each pizza's ID,
    toppings, and price.
    """
    id: int  # Unique id for the pizza
    toppings: str  # Type of the toppings on the pizza
    price: float  # Price of the pizza

    def __str__(self) -> str:
        """Shows each pizza's info, including ID, toppings, and price."""
        return (
            f"Pizza(ID={self.id}, Toppings={self.toppings}, "
            f"Price=${self.price:.2f})")

    # Getters
    def get_id(self) -> int:
        """Returns pizza's ID."""
        return self.id

    def get_toppings(self) -> str:
        """Returns pizza's toppings."""
        return self.toppings

    def get_price(self) -> float:
        """Returns pizza's price."""
        return self.price

    # Setters
    def set_id(self, new_id: int) -> None:
        """Sets pizza's ID."""
        if isinstance(new_id, int) and new_id >= 0:
            self.id = new_id
        else:
            raise ValueError("ID must be a positive integer.")

    def set_toppings(self, new_toppings: str) -> None:
        """Sets pizza's toppings."""
        if isinstance(new_toppings, str):
            self.toppings = new_toppings
        else:
            raise ValueError("All toppings must be strings.")

    def set_price(self, new_price: float) -> None:
        """Sets pizza's price."""
        if isinstance(new_price, (int, float)) and new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price must be a positive number.")
        

def main():
    """
    Main function to demonstrate usage of Wine and Pizza classes.
    
    Steps:
    1. Create a list of objects of type Wine and Pizza.
    2. Use a loop to display the IDs of all objects in the list.
    3. Count and display the number of objects for each class type.
    """

    # This list contains multiple objects from both the Wine and Pizza classes.
    items = [
        Wine(ID=10, name="Chardonnay", age=5),
        Wine(ID=22, name="Merlot", age=3),
        Pizza(id=12, toppings="Pepperoni", price=12.99),
        Pizza(id=25, toppings="Vegetarian", price=10.99),
        Pizza(id=34, toppings="Cheese", price=8.99),
        Wine(ID=31, name="Cabernet Sauvignon", age=8),
    ]

    # These counters will keep track of how many Wine and Pizza objects exist in the list.
    wine_count = 0
    pizza_count = 0

    # Loop through the list to display IDs and count objects by class
    print("Items in the list:")
    for item in items:
        # Display the ID of each object.
        # Use `get_ID()` for Wine and `get_id()` for Pizza.
        print(f"ID: {item.get_ID() if isinstance(item, Wine) else item.get_id()}")

        # Check the class of the object using isinstance and increment the appropriate counter.
        if isinstance(item, Wine):
            wine_count += 1
        elif isinstance(item, Pizza):
            pizza_count += 1

    # Show the total number of objects of each class after iterating through the list.
    print("\nSummary:")
    print(f"Number of Wine objects: {wine_count}")
    print(f"Number of Pizza objects: {pizza_count}")


# Run the main function when the script is executed directly.
if __name__ == "__main__":
    main()
