class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance = the square of x2 + y2
        max_heap = []

        for x, y in points:
            distance = -(x**2 + y**2)  # negative for max heap.
            if len(max_heap) < k:
                heapq.heappush(max_heap, (distance, [x, y]))
            else:
                heapq.heappushpop(max_heap, (distance, [x, y]))

        return [point for _, point in max_heap]


# Min heap version:
# minHeap = []
# for x, y in points:
#   dist = (x **2) + (y ** 2)
#   minHeap.append([dist, x, y])

# heapq.heapify(minHeap)
# res = []
# while k > 0:
#     dist, x, y = heapq.heappop(minHeap)
#     res.append([x,y])
#     k-=1
# return res
