class Solution:
    def reverse(self, x: int) -> int:
        s: str = str(x)
        if x < 0:
            s = s[1:]

        srev = ""

        for i in range(len(s) - 1, -1, -1):
            srev += s[i]

        y = int(srev)
        if x<0: y = -y

        if -(1<<31) >= y or y >= (1<<31) - 1:
            return 0
        else: return y

Solution().reverse(1563847412)
int()