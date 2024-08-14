class ContactNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class ContactSplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, name):
        if root is None or root.name == name:
            return root

        if name < root.name:
            if root.left is None:
                return root

            if name < root.left.name:
                root.left.left = self._splay(root.left.left, name)
                root = self._right_rotate(root)
            elif name > root.left.name:
                root.left.right = self._splay(root.left.right, name)
                if root.left.right is not None:
                    root.left = self._left_rotate(root.left)

            return root if root.left is None else self._right_rotate(root)
        else:
            if root.right is None:
                return root

            if name < root.right.name:
                root.right.left = self._splay(root.right.left, name)
                if root.right.left is not None:
                    root.right = self._right_rotate(root.right)
            elif name > root.right.name:
                root.right.right = self._splay(root.right.right, name)
                root = self._left_rotate(root)

            return root if root.right is None else self._left_rotate(root)

    def search_contact(self, name):
        self.root = self._splay(self.root, name)
        return self.root if self.root and self.root.name == name else None

    def add_contact(self, name):
        if self.root is None:
            self.root = ContactNode(name)
            return

        self.root = self._splay(self.root, name)

        if self.root.name == name:
            return  # Contact already exists, do nothing

        new_node = ContactNode(name)
        if name < self.root.name:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def delete_contact(self, name):
        if self.root is None:
            return

        self.root = self._splay(self.root, name)

        if self.root.name != name:
            return  # Contact not found

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root
            self.root = self._splay(self.root.left, name)
            self.root.right = temp.right

# Example usage:
contacts = ContactSplayTree()
contacts.add_contact("Alice")
contacts.add_contact("Bob")
contacts.add_contact("Charlie")

# Search for "Bob" - this will move Bob to the top of the tree
found = contacts.search_contact("Alice")
if found:
    print(f"Found: {found.name}")
else:
    print("Contact not found")

# After searching for "Bob", he becomes easier to find the next time
