from dataclasses import dataclass, field

@dataclass
class Member:
    """
    A class representing a member with a unique ID and name.
    """
    ID: int = field(default = 0)
    name: str = field(default="Unnamed Member")
    
    def __str__(self) -> str:
      """
      Magic method to return a string representation of the object
      """
      return f"Member[ID = {self.ID}, name = '{self.name}']"
      
    #Getter and Setter for ID
    def get_ID(self) -> int:
      """
      Getter for ID.
      returns:
          int: the unique ID for each memebr.
      """
      return self.ID
      
    def set_ID(self, new_ID: int) -> None:
      """
      Setter for ID. Make sure the ID is positive interger.
      Args:
          new_ID (int): the newID to set.
      """
      if isinstance(new_ID, int) and new_ID >0:
        self.ID = new_ID
      else:
        raise ValueError("ID is not a valid number.")
        
    #Getter and Setter for name
    def get_name(self) -> str:
      """
      Getter for the name
      Returns:
          str: the name of th member.
      """
      return self.name
      
    def set_name(self, new_name: str) -> None:
      """
      Setter for name. Make sure the name is not empty set.
      Args:
         new_name (str): the new name to set.
      """
      if isinstance(new_name, str) and new_name.strip():
            self.name = new_name
      else:
        raise ValueError("Name must be a non-empty string.")

# Main program
def main():
    # Create an object of Member class
    member = Member()

    # Test the default values
    print("Default Member:", member)

    # Set new ID and name using setters
    member.set_ID(101)
    member.set_name("John Doe")

    # Get the values using getters and print them
    print("Updated Member ID:", member.get_ID())
    print("Updated Member Name:", member.get_name())

    # Print the object to test __str__()
    print("Updated Member:", member)

if __name__ == "__main__":
    main()
