class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1 
        return l

            

print(Solution().searchInsert([1, 3 , 5 , 6], 2))