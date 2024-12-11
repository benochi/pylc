class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = int(str(abs(x))[::-1])
        if reversed == x:
            return True
        return False