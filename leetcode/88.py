class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = n + m - 1
        m -= 1
        n -= 1 
        while i >= 0:
            if n == -1:
                return
            elif m == -1:
                for i in range(n, -1, -1):
                    nums1[i] = nums2[i] 
            elif nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1 
            i -= 1

Solution().merge([4,5,6,0,0,0]
, 3 , [1,2,3], 3 )