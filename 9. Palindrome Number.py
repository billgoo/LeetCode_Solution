class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        if n == 1:
            return True
        
        for i in range(n // 2):
            if s[i] != s[n-1-i]:
                return False
        else:
            return True
            
        