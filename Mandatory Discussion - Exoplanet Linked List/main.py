from exoplanet_node import exoplanetNode

class LinkedList:
    """
    A custom linked list class to manage ExoplanetNode objects.
    This class provides methods for adding, removing, searching, and traversing the linked list.
    """
    def __init__(self):
        # Initialize an empty linked list.
        self.head = None
    
    def push(self, node):
        """
        Add a new node at the beginning of the linked list.
        :param node: An instance of exoplanetNode to add.
        """
        new_node = node
        new_node.next = self.head
        self.head = new_node

    def _print_nodes(self, node):
        """
        Recursively print all nodes starting from the given node.
        :param node: The starting node for printing.
        """
        if node is None:
            return
        else:
            self._print_nodes(node.next)
            print(node, "\n")
    
    def print_all_nodes(self):
        """
        Print all nodes in the linked list.
        """
        print("\nPrinting all nodes:")
        self._print_nodes(self.head)
    
    def _find_parent_node(self, child_ID):
        """
        Find the parent node of the node with the given ID.
        :param child_ID: The ID of the target node.
        :return: The parent node, or None if not found.
        """
        parent_node = self.head
        next_node = self.head.next if self.head else None
        while next_node:
            if next_node.ID == child_ID:
                return parent_node
            parent_node = next_node
            next_node = next_node.next
        return None

    def calculate_total_mass(self):
        """
        Calculate and return the total mass of all nodes in the list.
        :return: The total mass, or 0 if the list is empty.
        """
        total_mass = 0
        temp = self.head
        while temp:
            total_mass += temp.mass
            temp = temp.next
        return total_mass


def main():
    """
    Main function to create a linked list of exoplanets, perform operations, and display results.
    """
    # Create a linked list instance
    exoplanet_list = LinkedList()

    # Add sample exoplanets to the list
    exoplanet_list.push(exoplanetNode("TOI-5108 b", 0.073, 6.8, 2025, 32))
    exoplanet_list.push(exoplanetNode("TOI-5786 b", 0.114, 12.8, 2025, 0.22968))
    exoplanet_list.push(exoplanetNode("TOI-6016 b", 0.055, 4.0, 2024, 1.17))
    exoplanet_list.push(exoplanetNode("HD 101581 c", 0.0573, 6.2, 2025, 0.937))
    exoplanet_list.push(exoplanetNode("HD 73344 d", 6.7, 16, 2025, 2.55))

    # Display all nodes
    exoplanet_list.print_all_nodes()

    # Calculate and display the total mass
    total_mass = exoplanet_list.calculate_total_mass()
    print(f"Total Mass of Exoplanets: {total_mass}")


if __name__ == "__main__":
    main()
