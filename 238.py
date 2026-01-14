from typing import List
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right = 1
        sol = [1] * len(nums)

        for n in range(len(nums)-1):
            sol[n+1] = nums[n] * sol[n]

        for n in range(len(nums) - 1, 0, -1):
            right *= nums[n]
            sol[n-1] *= right

        return sol


        


         







    

print(Solution().productExceptSelf([1,2,3,4]))