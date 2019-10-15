class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # dp: p[i,j] = (p[i+1, j-1] and si==sj)
        # expand 1, 2, 3, n
        '''
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
        
        result = ""
        m= 0
        for i in range(n):
            for j in range(i, n):
                if j-i+1 > m and p[i][j]:
                    m = j-i+1
                    result = s[i:j+1]
                    
        return result
        '''
        
        # expand from center and have 2n-1 centers
        start, end = 0, 0
        
        n = len(s)
        for i in range(n):
            # center at one num
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1
            len1 = r - l - 1
            
            # center between 2 num
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1
            len2 = r - l - 1
            
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]