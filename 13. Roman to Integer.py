class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return d[s]
        
        l = [d[i] for i in s]
        prev = result = 0
        for i in range(n):
            result += d[s[i]]
            if d[s[i]] > prev:
                result -= 2 * prev
            prev = d[s[i]]
            
        return result
        