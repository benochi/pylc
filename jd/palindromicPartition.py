# Given a string s, the task is to find the minimum number of cuts needed for palindrome partitioning of the given string. 
# A partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome.

# Examples:  

# Input: s = “geek” 
# Output: 2 
# Explanation: We need to make minimum 2 cuts, i.e., “g | ee | k”.


# Input: s= “aaaa” 
# Output: 0 
# Explanation: The string is already a palindrome.


# Input: s = “ababbbabbababa” 
# Output: 3
# Explanation: We need to make minimum 3 cuts, i.e., “aba | bb | babbab | aba”.

# Constraints:
# 1 ≤ |s| ≤ 103
# s contain lowercase letters only
def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def pPart(s):
    n = len(s)
    dp = [float('inf')] * n  
    palindrome = [[False] * n for _ in range(n)]  


    for end in range(n):
        for start in range(end + 1):
            if s[start] == s[end] and (end - start <= 1 or palindrome[start + 1][end - 1]):
                palindrome[start][end] = True

    for i in range(n):
        if palindrome[0][i]:  
            dp[i] = 0
        else:
            for j in range(i):
                if palindrome[j + 1][i]:  
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

# Test cases
print(pPart("geek"))  # Output: 2
print(pPart("aaaa"))  # Output: 0
print(pPart("ababbbabbababa"))  # Output: 3
