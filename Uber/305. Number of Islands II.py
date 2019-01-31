class Solution:
    
    # default constructor, init all member data.
    def __init__(self):
        self.node = []     # This is init for each test case.
        self.counter = 0
    
    def numIslands2(self, m: 'int', n: 'int', positions: 'List[List[int]]') -> 'List[int]':
        for i in range(m):
            for j in range(n):
                self.node.append(-1)

        results = []
        for pos in positions:
            i, j = pos[0], pos[1]
            neighbours = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            root = i * n + j
            if self.node[root] == -1:
                self.node[root] = root
                self.counter += 1
            
            for nb in neighbours:
                x = i + nb[0] 
                y = j + nb[1]
                neighbor = x * n + y
                if y < 0 or y > n - 1 or x < 0 or x > m - 1 or self.node[neighbor] == -1:
                    continue
                if self.node[root] != self.Find(self.node[neighbor]):
                    self.node[root] = self.Find(self.node[neighbor])
                    root = self.node[root]
                    self.counter -= 1

            results.append(self.counter)
            
        return results
        

    def Find(self, x):
        if not x == self.node[x]:
            x = self.Find(self.node[x])
        return self.node[x]

if __name__ == "__main__":
    s = Solution()
    print(s.numIslands2(3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]))