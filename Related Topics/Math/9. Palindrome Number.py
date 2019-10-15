class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        
        p = 0
        while x > p:
            p = p * 10 + x % 10
            x //= 10
            
        return (x == p or x == p//10)