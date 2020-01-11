class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A or len(A) < 2:
            return -1
        
        A.sort()
        l, r = 0, len(A) - 1
        re = -1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                re = max(re, A[l] + A[r])
                l += 1
        
        return re
        