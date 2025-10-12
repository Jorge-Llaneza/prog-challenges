class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        for n in nums:
            if n == val:
                i += 1
        while i > 0:
            nums.remove(val)
            i -= 1        
        return len(nums)
    
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))