# Data Structures - Time and Space Complexities

## 1. Arrays

| Operation          | Average Time | Worst Time | Space Complexity |
| ------------------ | ------------ | ---------- | ---------------- |
| Access             | O(1)         | O(1)       | O(n)             |
| Search             | O(n)         | O(n)       | O(n)             |
| Insertion (End)    | O(1)         | O(1)       | O(n)             |
| Insertion (Middle) | O(n)         | O(n)       | O(n)             |
| Deletion (End)     | O(1)         | O(1)       | O(n)             |
| Deletion (Middle)  | O(n)         | O(n)       | O(n)             |

## 2. Linked Lists

| Operation         | Average Time | Worst Time | Space Complexity |
| ----------------- | ------------ | ---------- | ---------------- |
| Access            | O(n)         | O(n)       | O(n)             |
| Search            | O(n)         | O(n)       | O(n)             |
| Insertion (Start) | O(1)         | O(1)       | O(n)             |
| Insertion (End)   | O(1)         | O(1)       | O(n)             |
| Deletion (Start)  | O(1)         | O(1)       | O(n)             |
| Deletion (End)    | O(n)         | O(n)       | O(n)             |

## 3. Stacks

| Operation | Average Time | Worst Time | Space Complexity |
| --------- | ------------ | ---------- | ---------------- |
| Push      | O(1)         | O(1)       | O(n)             |
| Pop       | O(1)         | O(1)       | O(n)             |
| Peek      | O(1)         | O(1)       | O(n)             |

## 4. Queues

| Operation | Average Time | Worst Time | Space Complexity |
| --------- | ------------ | ---------- | ---------------- |
| Enqueue   | O(1)         | O(1)       | O(n)             |
| Dequeue   | O(1)         | O(1)       | O(n)             |
| Peek      | O(1)         | O(1)       | O(n)             |

## 5. Hash Tables

| Operation | Average Time | Worst Time | Space Complexity |
| --------- | ------------ | ---------- | ---------------- |
| Access    | N/A          | N/A        | O(n)             |
| Search    | O(1)         | O(n)       | O(n)             |
| Insertion | O(1)         | O(n)       | O(n)             |
| Deletion  | O(1)         | O(n)       | O(n)             |

> **Note**: Worst time complexity occurs when there are many collisions, resulting in O(n) search and insert time.

## 6. Binary Search Trees (BST)

| Operation | Average Time | Worst Time | Space Complexity |
| --------- | ------------ | ---------- | ---------------- |
| Access    | O(log n)     | O(n)       | O(n)             |
| Search    | O(log n)     | O(n)       | O(n)             |
| Insertion | O(log n)     | O(n)       | O(n)             |
| Deletion  | O(log n)     | O(n)       | O(n)             |

> **Note**: Worst time complexity occurs when the tree is unbalanced (e.g., skewed tree).

## 7. Heaps (Min/Max Heaps)

| Operation          | Average Time | Worst Time | Space Complexity |
| ------------------ | ------------ | ---------- | ---------------- |
| Access (min/max)   | O(1)         | O(1)       | O(n)             |
| Insertion          | O(log n)     | O(log n)   | O(n)             |
| Deletion (min/max) | O(log n)     | O(log n)   | O(n)             |

## 8. Graphs

| Representation   | Space Complexity | Search (BFS/DFS) | Insertion/Deletion (Edge) | Insertion/Deletion (Vertex) |
| ---------------- | ---------------- | ---------------- | ------------------------- | --------------------------- |
| Adjacency List   | O(V + E)         | O(V + E)         | O(1)                      | O(V)                        |
| Adjacency Matrix | O(V^2)           | O(V^2)           | O(1)                      | O(V^2)                      |

> **Note**: V = number of vertices, E = number of edges.

## 9. Tries (Prefix Trees)

| Operation | Average Time | Worst Time | Space Complexity |
| --------- | ------------ | ---------- | ---------------- |
| Insertion | O(m)         | O(m)       | O(26^m)          |
| Search    | O(m)         | O(m)       | O(26^m)          |
| Deletion  | O(m)         | O(m)       | O(26^m)          |

> **Note**: m = length of the key being inserted or searched.

## 10. Dynamic Programming Arrays (Memoization)

| Operation              | Average Time | Space Complexity |
| ---------------------- | ------------ | ---------------- |
| Memoization (1D array) | O(n)         | O(n)             |
| Memoization (2D array) | O(n \* m)    | O(n \* m)        |

> **Note**: n and m refer to the dimensions of the problem space, such as the length of a string or sequence.

## Summary

- **Time complexities** vary based on the structure and operation. For example, searching in a sorted array is faster with binary search (O(log n)), while in an unsorted array, linear search is required (O(n)).
- **Space complexities** typically scale with the size of the input data (e.g., O(n) for arrays and lists).
- Choosing the right data structure for a problem depends on the required operations and their expected frequency.
