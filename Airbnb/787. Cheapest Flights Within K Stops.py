class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        D = [(float('inf'), 0, src) for i in range(n)]
        E = [[float('inf') for i in range(n)] for j in range(n)]
        
        for i in range(n):
            E[i][i] = 0

        for airline in flights:
            E[airline[0]][airline[1]] = airline[2]

        D[src] = (0, 0, src)
        heapq.heapify(D)
        
        best = {}
        while D:
            cost, k, cur = heapq.heappop(D)
            if k > K + 1 or cost > best.get((k, cur), float('inf')):
                continue
            
            if cur == dst:
                return cost
            
            for i in range(len(E[cur])):
                if cost + E[cur][i] < best.get((k + 1, i), float('inf')):
                    heapq.heappush(D, (cost + E[cur][i], k + 1, i))
                    best[k + 1, i] = cost + E[cur][i]
        return -1
        