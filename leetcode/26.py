class Solution:
    def removeDuplicates(self, nums) -> int:
        previous = nums[0]
        count = len(nums)
        for n in nums[1:]:
            if n == previous:
                nums.remove(n)
                count -= 1
            previous = n
        return count
        
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
