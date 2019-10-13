class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        if len(s) != len(t):
            return False
        d = [0] * 26
        for i in s:
            d[ord(i) - ord('a')] += 1
        for j in t:
            d[ord(j) - ord('a')] -= 1
            if d[ord(j) - ord('a')] < 0:
                return False
        return True
        """
        # better solution
        if len(s) != len(t):
            return False
        
        d = dict()
        
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for i in t:
            if not i in d or d[i] <= 0:
                return False
            if i in d:
                d[i] -= 1
        
        return True