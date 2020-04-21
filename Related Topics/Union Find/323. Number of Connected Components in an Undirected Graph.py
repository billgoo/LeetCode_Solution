import collections

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        r_x, r_y = self.find(x), self.find(y)
        
        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        else:
            self.parent[r_x] = r_y
            if self.rank[r_y] == self.rank[r_x]:
                self.rank[r_y] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS O_n time and space
        """
        seen = set()
        
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        c = 0
        
        for u in range(n):
            if not u in seen:
                c += 1
                queue = collections.deque([u])
                while queue:
                    u = queue.popleft()
                    seen.add(u)

                    for v in adj_list[u]:
                        if not v in seen:
                            queue.append(v)
                            seen.add(v)
                # while ends
        # for ends
        return c
        """
        
        # union find ALG
        uf = UnionFind(n)
        
        for x, y in edges:
            uf.union(x, y)
        
        return len(set(uf.find(x) for x in range(n)))
            