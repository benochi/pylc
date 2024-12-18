class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        count = Counter(nums)
        outlier = float('-inf')

        for n in nums:
            count[n] -= 1
            totalSum -= n

            if totalSum % 2 == 0 and count[totalSum // 2] > 0:
                outlier = max(outlier, n)
            
            count[n] += 1
            totalSum += n
        return outlier
