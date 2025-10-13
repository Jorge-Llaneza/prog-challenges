class Solution:
    def plusOne(self, digits):
        p = len(digits) - 1
        for i in range(p+1 ):
            if digits[p] != 9:
                digits[p] += 1
                return digits
            else:
                digits[p] = 0
                p -= 1
        digits.insert(0,1)
        return digits
    
print(Solution().plusOne([9]))