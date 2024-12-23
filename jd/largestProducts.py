# Problem Statement:
# Largest products in k pairs

# You are given two integer arrays, nums1 and nums2, sorted in non-decreasing order, and an integer k.

# Define a pair (u, v), which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2),...,(uk, vk) with the largest products.

# Example 1:
# Input:
# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# k = 3
# Output:
# [[3, 6], [3, 4], [2, 6]]
# Explanation:
# The first 3 pairs with the largest products are:
# (3 x 6 = 18), (3 x 4 = 12), (2 x 6 = 12)

# Example 1:
# Input:
# nums1 = [1, 7, 11]
# nums2 = [2, 4, 6]
# k = 2
# Output:
# [[11, 6], [11, 4]]
# Explanation:
# The first 2 airs with the largest products are:
# (11 x 6 = 66), (11 x 4 = 44)

# Constraints:
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 are sorted in non-decreasing order
# 1 <= k <= 10^4
# k <= nums1.length x nums2.length
import heapq
def largestProducts(nums1, nums2, k):
    maxHeap = []
    heapq.heapify(maxHeap)
    res = []
    for n in nums1:
        for x in nums2:
            product = n * x 
            heapq.heappush(maxHeap, (-product, [n,x]))

    while k > 0 and maxHeap:
        product, values = heapq.heappop(maxHeap)
        res.append(values)
        k -= 1

    return res
print(largestProducts(nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 2))
print(largestProducts(nums1 = [1, 2, 3], nums2 = [2, 4, 6], k = 3))
print(largestProducts(nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 8))