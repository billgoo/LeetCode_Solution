class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # bi-search O_logn time
        """
        if num < 2:
            return True
        
        l, r = 2, num >> 1
        while l <= r:
            m = (l + r) >> 1
            p = m * m
            if p > num:
                r = m - 1
            elif p < num:
                l = m + 1
            else:
                return True
        
        return False
        """
        
        # Newton's method for root of a function O_logn time
        if num < 2:
            return True
        
        x = num >> 1
        while x * x > num:
            x = (x + num // x) >> 1
            
        return x * x == num