class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        # build graph G
        G = dict()
        for word in words:
            for letter in word:
                if letter not in G:
                    G[letter] = ''
                    
        while len(words) > 1:
            f = words.pop(0)
            l = words[0]
            for i in range(len(f)):
                if f[i] != l[i]:
                    G[f[i]] += l[i]
                    break
        return self.topoSort(G)
    
    
    def topoSort(self, G):
        in_degree = dict((u, 0) for u in G)
        for u in G:
            for v in G[u]:
                in_degree[v] += 1
                                    
        Q = [u for u in G if in_degree[u] == 0]
        
        if len(Q) == 0:
            return ""
        S = ""
        while Q:
            u = Q.pop()
            S += u
            for v in G[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    Q.append(v)
            del G[u]
        if len(G) > 0:
            return ""
        return S

        