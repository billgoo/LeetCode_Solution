class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row_0, col_0 = 1, 1
        col_0 = 1
        # matrix[0][0] = 0 is for row 0
        R, C = len(matrix), len(matrix[0])
        
        # set the first row for each col
        for i in range(R):
            if matrix[i][0] == 0:
                col_0 = 0
            
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for i in range(1, C):
                matrix[0][i] = 0
        if col_0 == 0:
            for i in range(R):
                matrix[i][0] = 0
        