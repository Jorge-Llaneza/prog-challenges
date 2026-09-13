class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0: return 0

        longest = 1

        seen = [False] * 256

        l=0
        r=0


        while r<len(s):   
            if not seen[ord(s[r])]:
                seen[ord(s[r])] = True
                r+= 1 
                longest = max(longest, r - l)
            else:
                seen[ord(s[l])] = False
                l += 1

        return longest
        