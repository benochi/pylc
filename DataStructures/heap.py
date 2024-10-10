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
# this only works in a complete binary tree
# leftChild = 2 * i
# rightChild = 2 * i + 1
# parent = i // 2 in python double slashes round down


class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):  # time complexity is height of tree O(logN)
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def pop(self):
        # always pop root, move last node to root then filter down.
        # O(logN)
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):  # 931 905 7931
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                # swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def readRoot(self):
        return self.heap[0]
