class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        
        for i in range(1, m):
            for j in range(1, n):
                top = grid[i - 1][j]
                left = grid[i][j - 1]
                grid[i][j] += min(top, left)
                
        return grid[m - 1][n - 1]