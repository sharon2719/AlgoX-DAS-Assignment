class TwoThreeTreeNode:
    def __init__(self):
        self.keys = []
        self.children = []

class TwoThreeTree:
    def __init__(self):
        self.root = TwoThreeTreeNode()

    def insert(self, key):
        print(f"Inserting {key} into the tree.")
        node = self.root
        if len(node.keys) == 0:
            node.keys.append(key)
        elif len(node.keys) == 1:
            if key < node.keys[0]:
                node.keys.insert(0, key)
            else:
                node.keys.append(key)
        else:
            if key < node.keys[0]:
                node.keys.insert(0, key)
            elif key > node.keys[1]:
                node.keys.append(key)
            else:
                node.keys.insert(1, key)
        print(f"Current tree keys: {self.root.keys}")

if __name__ == "__main__":
    tree = TwoThreeTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)