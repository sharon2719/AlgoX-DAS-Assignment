class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.preferred_child = None  # This keeps track of the preferred path

class TangoTree:
    def __init__(self):
        self.root = None

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self._right_rotate(x.parent)
                else:
                    self._left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._right_rotate(x.parent.parent)
                self._right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._left_rotate(x.parent.parent)
                self._left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self._left_rotate(x.parent)
                self._right_rotate(x.parent)
            else:
                self._right_rotate(x.parent)
                self._left_rotate(x.parent)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._splay(node)
        return node

    def search(self, key):
        node = self._search_tree(self.root, key)
        if node:
            self._splay(node)
        return node

    def _search_tree(self, node, key):
        if not node or key == node.key:
            return node
        if key < node.key:
            return self._search_tree(node.left, key)
        else:
            return self._search_tree(node.right, key)

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

# Example scenario: Autocomplete Feature in Search Engines
if __name__ == "__main__":
    autocomplete_tree = TangoTree()

    # Insert search suggestions into the system
    suggestions = ["apple", "app", "application", "apricot", "banana", "berry"]
    for suggestion in suggestions:
        autocomplete_tree.insert(suggestion)

    print("In-order traversal after insertions:", autocomplete_tree.in_order_traversal())
    # Expected output: ['app', 'apple', 'application', 'apricot', 'banana', 'berry']

    # User selects "application"
    search_node = autocomplete_tree.search("application")
    print("Searched suggestion:", search_node.key if search_node else "Not found")
    print("In-order traversal after selecting 'application':", autocomplete_tree.in_order_traversal())
    # Expected output: "application" should be closer to the root after this search.

    # User selects "banana"
    search_node = autocomplete_tree.search("banana")
    print("Searched suggestion:", search_node.key if search_node else "Not found")
    print("In-order traversal after selecting 'banana':", autocomplete_tree.in_order_traversal())
    # Expected output: "banana" should be moved closer to the root.

    # User selects "app"
    search_node = autocomplete_tree.search("app")
    print("Searched suggestion:", search_node.key if search_node else "Not found")
    print("In-order traversal after selecting 'app':", autocomplete_tree.in_order_traversal())
    # Expected output: "app" should be closer to the root.
