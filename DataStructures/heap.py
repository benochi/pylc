# Min heaps have the smallest value at the root node.
# The smallest value has the highest priority to be removed.
# Max heaps have the largest value at the root node.
# The largest value has the highest priority to be removed.

# priority Queue = Binary Heap which could be Min or Max
# min heaps are more common.
# balanced tree can only have missing nodes on bottom level
# heaps CAN have duplicates
# root always index 1, and we use arrays
# heap left to right fill in in array,
# this only works ina complete binary tree
leftChild = 2 * i
rightChild = 2 * i + 1
parent = i / 2
