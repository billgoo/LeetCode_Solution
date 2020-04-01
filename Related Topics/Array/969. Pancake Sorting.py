class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # get largest element to the first then swap to the tail
        # O_n^2 time and O_n space
        
        n = len(A)
        re = []
        
        for x in range(n, 1, -1):
            i = A.index(x)
            re += [i + 1, x]
            # A[:i:-1]: i之后的list的倒序
            A = A[:i:-1] + A[:i]
            
        return re
            