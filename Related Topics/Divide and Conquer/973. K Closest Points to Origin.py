class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) == 0:
            return -1
        dis = [[points[i][0] ** 2 + points[i][1] ** 2, i] for i in range(len(points))]
        
        def quickSelect(dis, l, r, K):
            if l == r:
                return dis[l][0]
            
            k = random.randint(l, r)
            dis[l], dis[k] = dis[k], dis[l]
            pivot = dis[l][0]
            pivot_i = l
            for i in range(l+1, r+1):
                if dis[i][0] < pivot:
                    pivot_i += 1
                    dis[i], dis[pivot_i] = dis[pivot_i], dis[i]
            dis[l], dis[pivot_i] = dis[pivot_i], dis[l]
            
            if pivot_i == K:
                return dis[pivot_i][0]
            elif pivot_i < K:
                return quickSelect(dis, pivot_i+1, r, K)
            elif pivot_i > K:
                return quickSelect(dis, l, pivot_i-1, K)
        
        num = quickSelect(dis, 0, len(points)-1, K-1)
        
        return [points[dis[i][1]] for i in range(K)]