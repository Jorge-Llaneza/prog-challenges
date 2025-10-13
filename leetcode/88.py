class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        nums3 = []
        if not nums2:
            return
        p1, p2 = 0, 0
        for i in range(m + n):
            if nums2[p2] > nums1[p1] and p1 < m:
                nums3.append(nums1[p1])
                p1 += 1 
            else: 
                nums3.append(nums2[p2])
                p2 += 1
        nums1 = nums3
        """
        Do not return anything, modify nums1 in-place instead.
        """
        