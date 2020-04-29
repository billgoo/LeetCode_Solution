class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        visit_count = 0
        buildings = sum([val for g in grid for val in g if val == 1])
        distance = [[0 for i in range(n)] for j in range(m)]
        seen = [[0 for i in range(n)] for j in range(m)]
        
        def BFS(x, y):
            seen[x][y] += 1
            
            Q = [[x, y, 0]]
            
            # c is the number of buildings reached from  (x, y)
            c = 1
            
            while Q:
                [node_x, node_y, dist] = Q.pop(0)
                for i, j in [(node_x + 1, node_y), (node_x - 1, node_y), \
                             (node_x, node_y + 1), (node_x, node_y - 1)]:
                    if 0 <= i < m and 0 <= j < n:
                        if seen[i][j] == visit_count - 1:
                            seen[i][j] += 1
                            if grid[i][j] == 0:
                                Q.append([i, j, dist + 1])
                                distance[i][j] += dist + 1
                            elif grid[i][j] == 1:
                                # connect to one other building
                                c += 1
            # if not connect graph, c != building
            # it is a trick for early determinated
            return c == buildings
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    # if seen == v_c, (x, y) must have been visited
                    visit_count += 1
                    if not BFS(x, y):
                        return -1
        
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and seen[i][j] == buildings:
                    ans = min(ans, distance[i][j])

        return ans if ans < float('inf') else -1