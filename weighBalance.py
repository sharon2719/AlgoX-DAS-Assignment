# defining the node class
class GradeNode:
    def __init__(self, key, weight=1):
        self.key = key
        self.weight =weight
        self.left = None
        self.right = None

class GradeWBTree:
    def __init__(self):
        self.root = None
    
    """ Update the weight of a node based on the weights of its subtrees """
    def _update_weight(self, node):
        if not node:
            return 0
        node.weight = 1 + self._get_weight(node.left) + self._get_weight(node.right)
        return node.weight
    
    """ helper function to get the weight value"""
    def _get_weight(self, node):
        return node.weight if node else 0
    
    """Right rotataion to balance the tree"""
    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        # Update weights after rotation
        self._update_weight(node)
        self._update_weight(new_root)
        return new_root
    
    """left rotation to balance the tree"""
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        # Update weights after rotation
        self._update_weight(node)
        self._update_weight(new_root)
        return new_root
    
    def _balance(self, node):
        """Balance the node based on the weights of its left and right subtrees"""
        if not node:
            return None
        left_weight = self._get_weight(node.left)
        right_weight = self._get_weight(node.right)

# Perform right rotation if the left subtree is too heavy
        if left_weight > 2 * right_weight:
            if self._get_weight(node.left.left) < self._get_weight(node.left.right):
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
# Perform left rotation if the right subtree is too heavy
        elif right_weight > 2 * left_weight:
            if self._get_weight(node.right.right) < self._get_weight(node.right.left):
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
    # Update the weight of the node and return it
        self._update_weight(node)
        return node

    def _insert(self, node, key):
        """# Recursive function to insert a key into the tree"""
        if not node:
            return GradeNode(key)
        if key < node.key :
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        # Balance the node after insertion
        return self._balance(node)
    
    def insert(self, key):
        # Public method to insert a key into the tree
        self.root = self._insert(self.root, key)

    def _in_order_traversal(self, node, result):
        # Perform an in-order traversal to retrieve keys in sorted order
        if not node:
            return
        self._in_order_traversal(node.left, result)
        result.append(node.key)
        self._in_order_traversal(node.right, result)

    def get_top_scores(self, n):
        # Get the top 'n' scores from the tree
        result = []
        self._in_order_traversal(self.root, result)
        return result[-n:]# Return the last 'n' elements (the highest scores)

# Example Usage
leaderboard = GradeWBTree()
scores = [55, 23, 87, 91, 47, 65, 12, 77, 89, 54]

# Insert scores into the leaderboard
for score in scores:
    leaderboard.insert(score)

# Retrieving the top 5 scores
top_scores = leaderboard.get_top_scores(5)
print("Top 5 Scores:", top_scores)
# Expected output: Top 5 Scores: [65, 77, 87, 89, 91]