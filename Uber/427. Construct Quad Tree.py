
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: 'List[List[int]]') -> 'Node':
        if not grid:
            return None
        
        n = len(grid)
        
        # is Leaf since only have one grid
        if all(grid[i][j]==1 for i in range(n) for j in range(n)):
            return Node(grid[0][0]==1, True, None, None, None, None)
        elif all(grid[i][j]==0 for i in range(n) for j in range(n)):
            return Node(grid[0][0]==1, True, None, None, None, None)
        else:
            topLeft = self.construct([row[:n//2] for row in grid[:n//2]])
            topRight = self.construct([row[n//2:] for row in grid[:n//2]])
            bottomLeft =  self.construct([row[:n//2] for row in grid[n//2:]])
            bottomRight = self.construct([row[n//2:] for row in grid[n//2:]])
            
            return Node('*', False,
                        topLeft, topRight, bottomLeft, bottomRight)


if __name__ == "__main__":
    s = Solution()
    s.construct([[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,0,0]])