class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        up, down = 1, 1
        maxLen = 1

        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                up = down + 1
                down = 1
            elif arr[i - 1] > arr[i]:
                down = up + 1
                up = 1
            else:
                up = down = 1

            maxLen = max(maxLen, up, down)

        return maxLen