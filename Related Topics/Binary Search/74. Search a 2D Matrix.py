class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        
        l, r = 0, row * col - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[m//col][m%col]:
                return True
            elif target < matrix[m//col][m%col]:
                r = m - 1
            else:
                l = m + 1
                
        return False
        