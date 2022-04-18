# 59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(n)]
        upper, lower, left, right = 0, n - 1, 0, n - 1
        count = 1
        while upper <= lower and left <= right:
            # 上
            if upper <= lower:
                for i in range(left, right + 1):
                    res[upper][i] = count
                    count += 1
                upper += 1
            # 右
            if left <= right:
                for i in range(upper, lower + 1):
                    res[i][right] = count
                    count += 1
                right -= 1
            # 下
            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res[lower][i] = count
                    count += 1
                lower -= 1
            # 左
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res[i][left] = count
                    count += 1
                left += 1
        return res

# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         re = [[0 for i in range(n)] for j in range(n)]

#         r, c, dr, dc = 0, 0, 0, 1
#         for i in range(n * n):
#             re[r][c] = i + 1
#             if re[(r+dr)%n][(c+dc)%n]:
#                 dr, dc = dc, -dr
#             r += dr
#             c += dc

#         return re
