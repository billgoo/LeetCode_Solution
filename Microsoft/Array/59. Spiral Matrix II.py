class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        re = [[0 for i in range(n)] for j in range(n)]
        
        r, c, dr, dc = 0, 0, 0, 1
        for i in range(n * n):
            re[r][c] = i + 1
            if re[(r+dr)%n][(c+dc)%n]:
                dr, dc = dc, -dr
            r += dr
            c += dc
        
        return re
        