class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):  # O(n)
        # 0-th is moved to to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # percolate down
            i = cur
            while 2 * i < len(self.heap):
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
                cur -= 1
