class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        #iterate twice
        for i in range(2 * n - 1, -1, -1): #iterate from the end twice
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()

            # if stack is not empty, the top element is the next greater
            if stack:
                result[i % n] = nums[stack[-1]]
            
            stack.append(i % n) # push current index onto the stack
        
        return result
