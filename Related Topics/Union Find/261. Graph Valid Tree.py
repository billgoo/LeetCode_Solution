class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1 for _ in range(n)]
        
    def find(self, x):
        root = x
        if root != self.parent[root]:
            self.parent[root] = self.find(self.parent[root])
        return self.parent[root]
    
    def union(self, x, y):
        r_x, r_y = self.find(x), self.find(y)
        
        if r_x == r_y:
            # have circle
            return False
        
        if self.size[r_x] > self.size[r_y]:
            self.parent[r_y] = r_x
            self.size[r_x] += self.size[r_y]
        else:
            self.parent[r_x] = r_y
            self.size[r_y] += self.size[r_x]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Advanced Graph Theory O_n time and space
        # exact n - 1 edges and fully connected
        """
        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        is_visited = set([0])
        queue = collections.deque([0])
        
        while queue:
            u = queue.popleft()
            for nei in adj_list[u]:
                if nei in is_visited:
                    # because it is un-directed graph
                    continue
                
                is_visited.add(nei)
                queue.append(nei)
                
        return len(is_visited) == n
        """
        
        # Advanced Graph Theory and union find ALG
        # O_n*alpha(n) time and O_n space
        if len(edges) != n - 1:
            return False
        
        unionFind = UnionFind(n)
        
        for u, v in edges:
            if not unionFind.union(u, v):
                return False
            
        return True