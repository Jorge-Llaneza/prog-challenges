class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inverted_result = []
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        while p1 >= 0 and p2 >= 0:
            carry = sum(int(a[p1]), int(b[p2]), carry, inverted_result)
            p1 -= 1
            p2 -= 1

        while p1 != -1:
            carry = sum(int(a[p1]), 0, carry, inverted_result)
            p1 -= 1
        while p2 != -1:
            carry = sum(int(b[p2]), 0, carry, inverted_result)
            p2 -= 1
        if carry :
            inverted_result.append(1)
        
        return "".join(str(n) for n in inverted_result[::-1])
    
def sum(a, b, carry, list) : # returns carry
    list.append(a^b^carry)
    return (a&b) | (a&carry) | (b&carry)

print(Solution().addBinary("1", "111"))
