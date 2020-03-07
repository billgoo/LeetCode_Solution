class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # dp: p[i,j] = (p[i+1, j-1] and si==sj)
        # expand 1, 2, 3, n
        # time n^2, space n^2
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
        # time n^2, space n
        '''
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
        '''
        
        # Manacher's Algorithm
        # time n, space n
        def add_boundary(s):
            # 为了使得算法中操作的字符串中字符个数始终为奇数，即中心对称
            new_s = "#"
            for c in s:
                new_s += c + "#"
            return new_s
        
        new_s = add_boundary(s)
        n = len(new_s)
        p = [0 for _ in range(n)]
        max_right, center = 0, 0
        max_len, start = 1, 0
        
        for i in range(n):
            if i < max_right:
                mirror = 2 * center - i
                # 算法核心步骤
                p[i] = min(max_right - i, p[mirror])
            # 以i为中心向左右扫描，其中中心旁边的p[i]个已经之前扫描过，所以跳过
            l, r = i - (p[i] + 1), i + (p[i] + 1)
            while l >= 0 and r < n and new_s[l] == new_s[r]:
                l -= 1; r += 1
                p[i] += 1
                
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
            
            if max_len < p[i]:
                max_len = p[i]
                start = (i - max_len) // 2
                
        return s[start: start + max_len]
        
        