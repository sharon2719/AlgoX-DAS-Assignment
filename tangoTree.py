class Node:
    def __init__(self, key):
        self.key = key # Value/key stored in the node
        self.right = None # pointer to the right child
        self.left = None # pointer to the left child
        self.parent = None #pinter to the parent node

class SimpleNumberTree:
    def __init__(self):
        self.root = None #Initialize the root of the tree as None

    def insert(self, key):
        """Inset a new key into the tree"""
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else: # Go to the right subtree
                if not current.right:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
    
    def serch(self, key):
        """Search for a key in the tree"""
        current = self.root
        while current:
            if key == current.key:
                return current # key is found
            elif key < current.key:
                current = current.left # Search in the left subtree
            else:
                current = current.right # Search in the right subtree
        return None # No key found
    
    def in_order_traversal(self, node, result):
        """Perform in-order-traversal of the tree"""

        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.key)
            self.in_order_traversal(node.right, result)
    
    def get_in_order_traversal(self):
        """Get the in-order traversal of the tree"""
        result = []
        self.in_order_traversal(self.root, result)
        return result
    

# usage example
if __name__ == "__main__":
    tree = SimpleNumberTree()

    # Inser elemets into the tree
    elements = [12,4,50,5,23,17]
    for element in elements:
        tree.insert(element)
    
    print(f"In order traversal afer insertion: ", tree.get_in_order_traversal())
    # Expected output: In order traversal afer insertion:  [4, 5, 12, 17, 23, 50]

# Searching for an element inside the tree
    search_result = tree.serch(4)
    print(f"Search result: {search_result.key if search_result else 'Not found'}")
    # Expected output if 4 is found: Search result: 4

 # Searching for a non-existant element inside the tree
    search_result = tree.serch(100)
    # Output when not found: Search result: Not found