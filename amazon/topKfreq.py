class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq,num in heap]
    
    #much easier without implemetning heap manually: count = Counter(nums)
        # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # return [num for num, freq in count.most_common(k)]