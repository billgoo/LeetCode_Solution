class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n > 1:
            mid = n // 2
            for i in range(0, mid):
                s[i], s[-i-1] = s[-i-1], s[i]
