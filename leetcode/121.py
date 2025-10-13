class Solution:
    def maxProfit(self, prices) -> int:
        maxp = 0
        l, r = 0, 1 
        while r < len(prices):
            if prices[l] < prices[r]:
                maxp = max(maxp, prices[r]-prices[l])
                r += 1
            else: 
                l = r
                r += 1
        return maxp

Solution().maxProfit([7,1,5,3,6,4])
                