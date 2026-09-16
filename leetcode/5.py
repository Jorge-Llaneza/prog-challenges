
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #preprocessing:

        if s == "": return ""

        ps = "@"
        for c in s:
            ps += f"#{c}"
        ps += "#$";

        longest, index = 1, 1

        for i in range(1, len(ps) - 1):
            j = 0
            l = 1
            while True:
                j += 1
                if ps[i + j] == ps[i-j]:
                    l += 1
                else: break

            if l > longest:
                longest = l
                index = i

        rets = ""

        if ps[index] != "#": rets += ps[index]
        for i in range(index + 1, index + longest):
            if ps[i] != "#":
                rets = f"{ps[i]}{rets}{ps[i]}"

        return rets


Solution().longestPalindrome("babad")