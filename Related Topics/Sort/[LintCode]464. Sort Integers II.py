class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        def qucikSort(A, left, right):
            if left >= right:
                return
            l, r = left, right
            key = A[right]
            
            while l < r:
                while l < r and A[l] <= key:
                    l += 1
                while l < r and A[r] >= key:
                    r -= 1
                    
                A[l], A[r] = A[r], A[l]
                
            A[r], A[right] = A[right], A[r]
            
            qucikSort(A, left, l - 1)
            qucikSort(A, r + 1, right)
                
        qucikSort(A, 0, len(A) - 1)
                    