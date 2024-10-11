class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for n in nums:
            maxHeap.append(-n)

        heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        res = maxHeap[0]
        return -res

    # Neetcode solution:
    k = len(nums) - 1

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)


# minHeap solution.
class Solution:
    def findKthLargest(self, nums, k):
        # Create a min-heap with the first `k` elements.
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate over the remaining elements.
        for num in nums[k:]:
            # If the current number is larger than the smallest in the heap, replace the root.
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        # The root of the min-heap is the `k`-th largest element.
        return min_heap[0]
