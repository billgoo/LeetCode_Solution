class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if not s:
            return ""
        
        re = []
        n = len(s)
        p = [[0 for i in range(n)] for j in range(n)]
        p[0][0] = 1
        for i in range(1, n):
            p[i][i] = 1
            if s[i-1] == s[i]:
                p[i-1][i] = 1
            
        for j in range(n):
            for i in range(j):
                if p[i+1][j-1] and (s[i]==s[j]):
                    p[i][j] = 1
                
        #print(p)
                
        m = 0
        for i in range(n):
            for j in range(n):
                if j - i + 1 > m and p[i][j]:
                    m = j - i + 1
                    re = [i, j]
        
        return s[re[0]:re[1]+1]