class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        hashmap = [0 for i in range(128)]
        length = 0
        k = 0
        for i in range(len(s)):
            if hashmap[ord(s[i])-ord(' ')] != 0:
                k = max(hashmap[ord(s[i])-ord(' ')], k)
            length = max(length, i - k + 1)
            hashmap[ord(s[i])-ord(' ')] = i + 1
        return length