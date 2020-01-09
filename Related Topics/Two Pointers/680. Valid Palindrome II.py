class Solution:
    def validPalindrome(self, s: str) -> bool:
        # remove head and tail if they can form palindrome
        i = 0
        n = len(s)
        while i < len(s) and s[i] == s[~i]:
            i += 1
        
        # validate the remain part for two cases
        return s[i+1:n-i] == s[i+1:n-i][::-1] or s[i:n-i-1] == s[i:n-i-1][::-1]
        