class TwoThreeFourTreeNode:
    def __init__(self):
        self.keys = []
        self.children = []

class TwoThreeFourTree:
    def __init__(self):
        self.root = TwoThreeFourTreeNode()

    def insert(self, key):
        print(f"Inserting {key} into the tree.")
        node = self.root
        if len(node.keys) < 3:
            node.keys.append(key)
            node.keys.sort()
        else:
            print("Node is full. Splitting required (not implemented here).")
        print(f"Current tree keys: {self.root.keys}")

if __name__ == "__main__":
    tree = TwoThreeFourTree()
    tree.insert(15)
    tree.insert(25)
    tree.insert(5)
    tree.insert(30)