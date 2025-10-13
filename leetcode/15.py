from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        le = len(nums)
        for i, n in enumerate(nums):
            if i == le - 2:
                break
            if i != 0:
                if n == nums[i-1]: 
                    continue
            l = i + 1
            r = le - 1
            while l != r:
                if n + nums[l] + nums[r] > 0:
                    r -= 1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    sol.append([n, nums[l], nums[r]])
                    if nums[l] == nums [r]:
                        l = r
                        continue
                    l += 1
        return sol
Solution().threeSum([0,0,0,0])

            