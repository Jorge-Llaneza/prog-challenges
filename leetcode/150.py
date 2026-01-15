from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if not isOP(t):
                stack.append(int(t))
                pass
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(poleval(n2, n1, t))
        return int(stack[0])
        
def isOP(s):
    match s:
        case "*":
            return True
        case "/":
            return True
        case "+":
            return True
        case "-":
            return True
        case _:
            return False
def poleval(first, second, op):
    match op:
        case "*":
            return first * second 
        case "/":
            return int(first / second )
        case "+":
            return first + second 
        case "-":
            return first - second 

print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))
