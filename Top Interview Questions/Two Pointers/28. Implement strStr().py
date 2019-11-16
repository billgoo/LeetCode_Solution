class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        
        i = 0
        while i <= len(haystack) - len(needle):
            count, j = 0, 0
            while j < len(needle) and haystack[i] == needle[j]:
                count += 1; i+= 1; j += 1
            if count == len(needle):
                return i - count
            else:
                i = i - count + 1
                
        return -1