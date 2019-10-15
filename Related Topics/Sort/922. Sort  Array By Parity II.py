class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        x = 1
        y = 0
        B = [0] * len(A)
        for i in range(len(A)):
            if A[i] % 2:
                B[x] = A[i]
                x += 2
            else:
                B[y] = A[i]
                y += 2
        return B