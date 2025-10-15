class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k >= len(nums)-1:
            return not len(nums) == len(set(nums))
        d = {}
        for i in range(k+1):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return True
        for i in range(k+1, len(nums)):
            num = nums[i]
            if num not in d:
                d[num] = 0
            if d[num] == 1 and num != nums[i-k-1]:
                return True
            elif d[num] != d[nums[i-k-1]]:
                d[nums[i-k-1]] = 0
                d[num] = 1
        return False 
arr = [1,0,1,1]

print(Solution().containsNearbyDuplicate(arr, 1))
print(len(arr))

        