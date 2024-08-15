# Comprehensive Python Implementations of Binary Trees
## 1. Splay Trees
### Characteristics:

Splay trees are a type of binary search tree that adjusts itself automatically.
When you `search for`, `insert`, or `delete` a node, the tree rearranges itself so that the accessed node moves to the top (root) of the tree.
This rearrangement helps make the tree faster for elements you use often, keeping frequently used elements near the top.

### Applications:

Splay trees are useful for speeding up access to data that is used repeatedly, like in caches or memory management systems.
They are especially effective in situations where some data is accessed much more frequently than others (like the 80-20 rule, where 80% of the accesses are to 20% of the data).A good example is searching for frequently used contact as seen in [here](splay-tree.py)

## 2. B-trees
### Characteristics:

B-trees are a kind of balanced tree that keeps data sorted and allows you to `search`, `add`, and `delete` data quickly.
Unlike regular binary trees, B-trees can have `more than two child nodes`, which helps keep the tree balanced and efficient.
They are designed to work well with systems that deal with large blocks of data, like databases and file systems.

### Applications:

B-trees are commonly used in databases and file systems because they can efficiently handle large amounts of data and keep it organized.
They are perfect for situations where the data structure needs to stay balanced, even when adding or removing a lot of data.
B-trees are also ideal for systems that need to access large chunks of data at once, like reading from or writing to a disk. A good real-life example is searching for a book according to its ISBN as shown [here](b-tree.py) 

## 3. Tango Trees
### Characteristics:
1. Self-Adjusting Structure: Tango trees maintain a set of dynamic paths know as `preferred paths`, which represent the most recent accessed parts of the tree and the tree structure is adjusted to optimize access to these paths.
2. Competitive Access Time: Tango trees perfomance is within a constant factor of the optimak statis binary tree of any sequence of operations, making then to be known to be `O(log n) competitive`.

### Applications
 1. Network Routing Table: Tango trees can optimize routing tables by keeping frequently accessed routes closer to the top, thus speeding up the lookup process and improving packet forwarding efficiency.
2. Caching Systems: Tango trees can be employed to manage cache entries, ensuring that frequently accessed data is quicker to retrieve. This helps in optimizing the performance of caching mechanisms by minimizing the access time for commonly requested data.