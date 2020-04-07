class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # DFS O_m*n time and m*n space
        coord = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                stack = []
                stack.append([i, j])
                # dfs
                while stack:
                    index = stack.pop()
                    if grid[index[0]][index[1]] == "1":
                        for c in coord:
                            x = index[0] + c[0]
                            y = index[1] + c[1]
                            if x>=0 and x<m and y>=0 and y<n:
                                if grid[x][y] == "1":
                                    stack.append([x, y])
                                else:
                                    grid[x][y] = "-1"
                    grid[index[0]][index[1]] = "-1"
                # end while
                counter += 1
        # end out for
        return counter
        
        # BFS O_m*n time and min(m, n) space for queue
        """
        if not grid:
            return 0
        
        coordinate = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        counter = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    counter += 1
                    queue = [[i, j]]
                    while queue:
                        node = queue.pop(0)
                        if grid[node[0]][node[1]] == '1':
                            grid[node[0]][node[1]] = '-1'
                            for co in coordinate:
                                if 0 <= node[0] + co[0] < m and\
                                    0 <= node[1] + co[1] < n:
                                    if grid[node[0]+co[0]][node[1]+co[1]]\
                                        == '1':
                                        queue.append([
                                            node[0]+co[0], node[1]+co[1]
                                        ])
        
        return counter
        """          