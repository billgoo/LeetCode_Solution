import collections

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    
        days = 0
        neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            days += 1
            size = len(queue)
            
            for i in range(size):
                [x, y] = queue.popleft()
                for nx, ny in neighbor:
                    nei_x, nei_y = x + nx, y + ny
                    if 0 <= nei_x < m and 0 <= nei_y < n:
                        if grid[nei_x][nei_y] == 0:
                            grid[nei_x][nei_y] = 1
                            queue.append([nei_x, nei_y])
                            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
            
        return days - 1