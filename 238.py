from typing import List
import math
class Solution:
    nums = []
    sol = []
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.sol = [0 for _ in nums]

        self.productExceptSelfN(0, len(nums) - 1, 1)
        return self.sol

    def productExceptSelfN(self, p1, p2, n):
        if p2 == p1 + 1:
            self.sol[p1] = n * self.nums[p2]
            self.sol[p2] = n * self.nums[p1]
        elif p1 == p2:
            self.sol[p1] = n
        else:
            p_middle: int = int((p1 + p2) / 2)

            n1 = math.prod(self.nums[p_middle + 1: p2 + 1]) * n
            self.productExceptSelfN(p1, p_middle, n1)

            n2 = math.prod(self.nums[p1: p_middle+1]) * n
            self.productExceptSelfN(p_middle + 1, p2, n2)
        return
    

print(Solution().productExceptSelf([1,2,3,4,5]))