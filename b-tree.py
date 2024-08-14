class LibraryNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for the number of books (keys))
        self.leaf = leaf  # True if node is a leaf. Otherwise, False
        self.keys = []  # List of book identifiers (keys) in the node
        self.children = []  # List of child nodes (pointers)

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.leaf:
            # Insert the new book identifier at the appropriate position
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1

            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = LibraryNode(t, y.leaf)

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

class LibraryBTree:
    def __init__(self, t):
        self.root = LibraryNode(t, True)
        self.t = t  # Minimum degree

    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node

        if node.leaf:
            return None

        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = LibraryNode(self.t, False)
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root

        self.root.insert_non_full(key)

# Example usage:
library = LibraryBTree(3)  # A B-tree with a minimum degree of 3
library.insert("978-3-16-148410-0")  # ISBN for Book A
library.insert("978-0-306-40615-7")  # ISBN for Book B
library.insert("978-1-4028-9462-6")  # ISBN for Book C

# Search for a book by its ISBN
found = library.search("978-0-306-40615-7")
if found:
    print(f"Book found with ISBN: {found.keys}")
else:
    print("Book not found")
