class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        maxFreqCount = 0
        
        for v in count.values():
            if v == maxFreq:
                maxFreqCount += 1

        intervals = (maxFreq - 1) * (n + 1) + maxFreqCount

        return max(intervals, len(tasks))