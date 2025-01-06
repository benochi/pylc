from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        output = []
        count = Counter(nums)

        for key, val in count.items():
            if val > freq:
                output.append(key)

        return output
    
# Optimal
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        freq = len(nums) // 3
        result = []
        if count1 > freq:
            result.append(candidate1)
        if count2 > freq:
            result.append(candidate2)

        return result