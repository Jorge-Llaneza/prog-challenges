import math
class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 0
        for i in range(0, int(n/2) + 1):
            sum += math.comb(n - i, i)
        return sum
print(Solution(). climbStairs(6))
