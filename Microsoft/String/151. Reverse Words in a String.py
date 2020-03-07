class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. clean spaces
        # remove the head and tail
        i = 0
        n = len(s)
        new_s = []
        
        while i < n:
            # remove front
            while i < n and s[i] == " ":
                i += 1
            
            # add word
            while i < n and s[i] != " ":
                new_s.append(s[i])
                i += 1
            
            # remove middle and tail
            while i < n and s[i] == " ":
                i += 1
            
            # add one space between word
            if i < n:
                new_s.append(" ")
        
        # 2. reverse the whole string
        n = len(new_s)
        i, j = 0, n - 1
        while i < j:
            new_s[i], new_s[j] = new_s[j], new_s[i]
            i += 1
            j -= 1
        
        # 3. reverse char in each word
        i = j = 0
        while i < n:
            # skip space
            while i < n and new_s[i] != " ":
                i += 1
            
            # swap
            left, right = j, i - 1
            while right < n and left < right:
                new_s[left], new_s[right] = new_s[right], new_s[left]
                left += 1
                right -= 1
                
            j = i + 1
            i += 1
            
        return ''.join(new_s)
        