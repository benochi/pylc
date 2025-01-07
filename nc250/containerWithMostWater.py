class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        volume = 0

        while l < r:
            diff = r - l
            volume = max(volume, min(height[l], height[r]) * diff)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return volume