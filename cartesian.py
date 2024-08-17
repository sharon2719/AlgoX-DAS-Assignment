class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """ Function to build a Cartesian Tree from an array. """
    stack = []
    root = None
    
    for i in range(len(arr)):
        node = Node(arr[i])
        last_popped = None
        
        # Maintain a decreasing stack (as per max-heap property)
        while stack and stack[-1].key > node.key:
            last_popped = stack.pop()
        
        if stack:
            stack[-1].right = node
        else:
            root = node
        
        node.left = last_popped
        stack.append(node)
    
    return root

def inorder_traversal(node):
    """ Inorder traversal of Cartesian Tree (should return the original array) """
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

# Example usage:
arr = [3, 2, 6, 1, 9]
root = build_cartesian_tree(arr)
inorder_traversal(root)  # Output should be the same as input array
