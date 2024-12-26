class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            # Function to determine if we can split the array into at most k parts
            # with each part having a sum <= max_sum
            current_sum = 0
            splits = 1
            for num in nums:
                if current_sum + num > max_sum:
                    splits += 1
                    current_sum = num
                    if splits > k:
                        return False
                else:
                    current_sum += num
            return True

        # Binary search to find the minimal largest sum
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left