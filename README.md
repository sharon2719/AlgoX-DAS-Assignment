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
They are perfect for situations where the data structure needs to stay balanced, even when adding or removing a lot of data.B-trees are also ideal for systems that need to access large chunks of data at once, like reading from or writing to a disk. A good real-life example is searching for a book according to its ISBN as shown [here](b-tree.py)


## 3. 2-3 Tree

### Characteristics:

A 2-3 Tree is a special kind of binary search tree that keeps itself balanced. In this tree:

- Every node (except the leaves) can have 2 or 3 children.
- All the leaves (end nodes) are at the same level, which means the tree is balanced.

### Applications:

2-3 Trees are especially useful in database systems where we need to keep data sorted and balanced, making search operations faster. They are often used in file systems to manage large amounts of data efficiently.

### Python Implementation:

You can find the Python code for the 2-3 Tree [here](two_three_tree.py).

## 4. 2-3-4 Tree

### Characteristics:

A 2-3-4 Tree is an extension of the 2-3 Tree. It allows each node to have 2, 3, or 4 children. This tree stays balanced by splitting nodes as new elements are added, which ensures efficient search and insert operations.

### Applications:

2-3-4 Trees are used in databases and file systems, particularly in implementations of B-trees. They are ideal for managing large datasets where balanced search times are crucial.

### Python Implementation:

You can find the Python code for the 2-3-4 Tree [here](two_three_four_tree.py).

## Red-Black Trees

### Characteristics
Red-Black Trees are a type of self-balancing binary search tree where each node contains an extra bit for denoting the color of the node, either red or black. This ensures the tree remains balanced during insertions and deletions, guaranteeing that the longest path from the root to a leaf is no more than twice as long as the shortest path.

### Key properties include

Root Property: The root is always black.
Red Property: Red nodes cannot have red children (no two reds in a row).
Black Property: Every path from a node to its descendant NULL nodes must have the same number of black nodes.

### Applications
Red-Black Trees are commonly used in scenarios where maintaining a balanced tree is crucial for ensuring optimal time complexity for insertion, deletion, and lookup operations. Typical use cases include:

Associative Arrays: Many programming languages and libraries use Red-Black Trees to implement dictionaries or maps, ensuring fast data retrieval.
Linux Kernel: Red-Black Trees are utilized in the Linux kernel to manage process scheduling efficiently.
Databases: Red-Black Trees are often used in database indexing to ensure quick lookups and modifications.


## Binary Search Trees (BST)

### Characteristics:
A Binary Search Tree (BST) is a type of binary tree where each node has the following properties:

Left Subtree Property: All nodes in the left subtree of a node contain values less than the node’s value.
Right Subtree Property: All nodes in the right subtree of a node contain values greater than the node’s value.
No Duplicates: BSTs typically do not allow duplicate values. If duplicates are allowed, they are usually stored in a specific way (e.g., all duplicates in the right subtree).
BSTs are useful for efficient searching, insertion, and deletion operations, typically with a time complexity of O(log n) in the average case.

## Applications
BSTs are widely used in applications that require dynamic data structure management with quick lookup, insertion, and deletion operations. Some common use cases include:

Database Indexing: BSTs can be used to implement indexes, allowing quick search operations within databases.
Memory Management: Operating systems use BSTs to manage memory and prioritize processes.
Autocomplete Systems: BSTs can be used to implement autocomplete suggestions, by storing and efficiently searching through a list of words.


## 3. Tango Trees
### Characteristics:
i. Self-Adjusting Structure: Tango trees maintain a set of dynamic paths know as `preferred paths`, which represent the most recent accessed parts of the tree and the tree structure is adjusted to optimize access to these paths.
ii. Competitive Access Time: Tango trees perfomance is within a constant factor of the optimak statis binary tree of any sequence of operations, making then to be known to be `O(log n) competitive`.

### Applications
i. Network Routing Table: Tango trees can optimize routing tables by keeping frequently accessed routes closer to the top, thus speeding up the lookup process and improving packet forwarding efficiency.
ii. Caching Systems: Tango trees can be employed to manage cache entries, ensuring that frequently accessed data is quicker to retrieve. This helps in optimizing the performance of caching mechanisms by minimizing the access time for commonly requested data.

4. Weight-Balanced Tree
### Characteristics
i. Balance Condition: In WBT, a node is considered balanced if the ratio between the weights of its left and right subtrees satisfies a predefined condition. A common balance condition is that the weight of one subtree should not exceed the weight of the other subtree by more than a certain factor (usually a constant like 2).
ii. Rotation: To maintain balance after insertions or deletions, WBTs use rotations (just like AVL or Red-Black trees). The idea is to perform a rotation that redistributes the nodes to maintain the balance condition.

### Applications

- WBTs are mainly used in real-time systems, Game and AI, and Netwotk Routes
- These applications benefit from the properties of WBTs, such as efficient balancing based on weights, which ensures that operations remain fast even as the dataset changes. By maintaining logarithmic time complexity for operations, WBTs are suitable for a wide range of dynamic and performance-critical applications.

5. Cartesian Tree
### Characteristics
A Cartesian Tree is a binary tree derived from a sequence of numbers. It combines properties of a heap and a binary search tree.
Heap Property: Every node in the tree has a value greater than or equal to any value in its subtree (max-heap).
Binary Search Tree (BST) Property: Inorder traversal of the Cartesian tree results in the original sequence of numbers.

### Applications
Range Minimum Query (RMQ): Cartesian trees are often used for RMQ problems where you need to quickly find the minimum element in a range of an array.
Suffix Array Construction: Cartesian trees help in efficiently building suffix arrays, which are used in text processing and string matching algorithms.
Priority Queue Implementation: Since a Cartesian tree combines heap properties, it can also be used to implement priority queues.

6. Segment Tree
### Characteristics
A Segment Tree is a binary tree used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point efficiently.
Each node represents an interval, and the tree is typically built to support efficient range queries and updates.

### Applications
Range Queries: Segment trees are used for answering range queries like sum, minimum, maximum, and greatest common divisor (GCD) over a segment of an array.
Dynamic Range Queries: Unlike other data structures, Segment trees allow modifications to the array, with queries still being processed in logarithmic time.
