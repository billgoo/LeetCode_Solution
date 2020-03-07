class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_string(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        # reverse string
        n = len(s)
        reverse_string(s, 0, n - 1)
        
        # reverse word
        start = end = 0
        while end < n:
            while end < n and s[end] != " ":
                end += 1
            reverse_string(s, start, end - 1)
            end += 1
            start = end
            