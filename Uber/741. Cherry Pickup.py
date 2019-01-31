class Solution:
    def cherryPickup(self, grid: 'List[List[int]]') -> 'int':
        n = len(grid)
        dp = [[float('-inf')] * n for _ in range(n)]
        
        dp[0][0] = grid[0][0]
        
        for step in range(1, 2 * n - 1):
            temp = [[float('-inf')] * n for _ in range(n)]
            # set the right move of person 1 & 2
            for i in range(max(0, (step - n + 1)), min(n, step + 1)):
                for j in range(max(0, (step - n + 1)), min(n, step + 1)):
                    if grid[i][step - i] == -1 or grid[j][step - j] == -1:
                        continue
                    if i != j:
                        temp[i][j] = max(grid[i][step - i] + grid[j][step - j]
                                         + dp[r1][r2] for r1 in (i - 1, i)
                                         for r2 in (j - 1, j)
                                         if r1 >= 0 and r2 >= 0)
                    else:
                        temp[i][j] = max(grid[i][step - i]
                                         + dp[r1][r2] for r1 in (i - 1, i)
                                         for r2 in (j - 1, j)
                                         if r1 >= 0 and r2 >= 0)
            # end one move of person
            dp = temp
        return dp[n - 1][n - 1] if dp[n - 1][n - 1] >= 0 else 0