class Solution:
    i=0

    def eatWhitespaces(self):
        while self.i < len(self.s) and self.s[self.i] == " ":
            self.i+=1
    def eatZeroes(self):
        while self.i < len(self.s) and self.s[self.i] == "0":
            self.i+=1

    def sign(self):
        if self.i >= len(self.s): return

        c = self.s[self.i]
        if c == "+":
            self.i+=1
            return "+"
        if c == "-": 
            self.i+=1
            return "-"
        else:
            return "+"

    def myAtoi(self, s: str) -> int:
        if s=="": return 0

        self.s = s
        self.eatWhitespaces()
        sign = self.sign()
        self.eatZeroes()

        res=0
        while self.i<len(s) and (ord("0") <= ord(s[self.i]) <= ord("9")):
            res = int(s[self.i]) + res*10
            self.i+=1

        if sign == "-": res = -res

        if res > (1<<31) -1: return (1<<31) -1
        elif res < -(1<<31): return -(1<<31)
        else: return res

Solution().myAtoi(" ")