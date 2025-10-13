class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)
        d = {}
        for num in nums:
            if d.get(num, 0) == 0:
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.values():
            if v > l/2:
                return k