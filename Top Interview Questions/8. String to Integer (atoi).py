import sys

class Solution:
    def myAtoi(self, str: str) -> int:
        l = list(str.strip())
        if len(l) == 0:
            return 0
        
        if l[0] == '-':
            sign = -1
            del l[0]
        else:
            sign = 1
            if l[0] == '+':
                del l[0]
                
        p, i = 0, 0
        while i < len(l) and l[i].isdigit():
            p = p * 10 + int(l[i])
            i += 1
            
        return max(-2**31, min(sign*p, 2**31-1))