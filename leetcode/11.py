class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = min(height[l], height[r]) * (r - l)
        while l != r:
            if height[l] > height[r]:
                r -= 1
                maxArea = max(maxArea, min(height[r], height[l]) * (r-l))
            else:
                l += 1
                maxArea = max(maxArea, min(height[r], height[l]) * (r-l))
        return maxArea
                            
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))


 