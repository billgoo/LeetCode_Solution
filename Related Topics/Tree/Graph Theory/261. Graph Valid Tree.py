import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Advanced Graph Theory O_n time and space
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