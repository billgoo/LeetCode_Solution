class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        obj = collections.Counter(magazine)
        d = {}
        for k, v in obj.items():
            d[k] = v
            
        for l in ransomNote:
            if l in d and d[l] > 0:
                d[l] -= 1
            else:
                return False
            
        return True