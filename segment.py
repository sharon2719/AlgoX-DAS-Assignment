class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)
    
    def build(self, arr):
        """Build the segment tree by inserting the input array in the leaf nodes."""
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
    
    def update(self, pos, value):
        """Function to update a tree node."""
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.tree[pos << 1] + self.tree[pos << 1 | 1]
    
    def range_query(self, left, right):
        """Function to perform range query."""
        res = 0
        left += self.n
        right += self.n + 1
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
print(seg_tree.range_query(1, 3))  # Sum from index 1 to 3 => 3 + 5 + 7 = 15
seg_tree.update(1, 10)  # Update index 1 to value 10
print(seg_tree.range_query(1, 3))  # Sum from index 1 to 3 => 10 + 5 + 7 = 22
