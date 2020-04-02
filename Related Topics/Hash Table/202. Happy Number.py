class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_happy(x):
            ans = 0
            while x > 0:
                ans += (x % 10) ** 2
                x //= 10
            return ans
        
        s = {n}
        
        while n != 1:
            n = sum_happy(n)
            
            # if it is a infinite loop
            if n in s:
                return False
            s.add(n)
            
        return True
        