# In an N by N square grid, each cell is either empty (0) or blocked (1).
# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
# 解法：BFS：层次遍历
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = [[0, 0]]
        length = 1  # level
        while q:
            l = len(q)
            
            for _ in range(l):
                r, c = q.pop(0)
                if [r, c] == [m - 1, n - 1]:
                    return length
                
                if grid[r][c] == 0:
                    grid[r][c] = 1
                    for rp in [-1, 0, 1]:
                        for cp in [-1, 0, 1]:
                            if 0 <= r + rp < m and 0 <= c + cp < n:
                                if grid[r + rp][c + cp] == 0:
                                    q.append([r + rp, c + cp])
                                
            length += 1
            
        return -1
        
# Runtime: 784 ms, faster than 34.38% of Python3 online submissions for Shortest Path in Binary Matrix.
# Memory Usage: 14.6 MB, less than 83.86% of Python3 online submissions for Shortest Path in Binary Matrix.
