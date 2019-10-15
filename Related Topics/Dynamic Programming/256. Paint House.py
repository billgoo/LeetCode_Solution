class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        
        for i in range(1, n):
            temp = [j for j in costs[i]]
            for j in range(3):
                costs[i][j] = temp[j] + min(costs[i - 1][(j + 1) % 3], costs[i - 1][(j + 2) % 3])
        
        return min(costs[n - 1])
        