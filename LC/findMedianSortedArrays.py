class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge arrays then find median efficiently. log M + N worst case
        # for log we want binary search
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = math.floor(total / 2)

        if len(b)< len(a):
            a,b = b,a
        
        l, r = 0, len(a) -1
        while True:
            i = (l + r) // 2 #find midpoint
            j = half - i - 2 #- 2 handles j and i starting at 0

            aLeft = a[i] if i >= 0 else float("-infinity")
            aRight = a[i + 1] if (i+1) < len(a) else float("infinity")
            bLeft = b[j] if j >= 0 else float("-infinity")
            bRight = b[j + 1] if (j+1) < len(b) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                # odd
                if total % 2:
                    return min(aRight, bRight)
                # even
                return (max(aLeft, bLeft) + min(aRight,bRight)) / 2
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
        
        
        