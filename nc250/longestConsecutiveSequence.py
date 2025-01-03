class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for n in numSet:
            if n - 1 not in numSet: 
                length = 0
                current = n

                while current in numSet:
                    length += 1
                    current += 1

                maxLength = max(maxLength, length)

        return maxLength