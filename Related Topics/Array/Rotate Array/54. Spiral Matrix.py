# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        res = []
        upper, lower, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while upper <= lower and left <= right:
            # 上
            if upper <= lower:
                for i in range(left, right + 1):
                    res.append(matrix[upper][i])
                upper += 1
            # 右
            if left <= right:
                for i in range(upper, lower + 1):
                    res.append(matrix[i][right])
                right -= 1
            # 下
            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res.append(matrix[lower][i])
                lower -= 1
            # 左
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         re = []
#         if not matrix:
#             return re

#         r1, r2 = 0, len(matrix) - 1
#         c1, c2 = 0, len(matrix[0]) - 1

#         while r1 <= r2 and c1 <= c2:
#             for c in range(c1, c2+1):
#                 re.append(matrix[r1][c])
#             for r in range(r1+1, r2+1):
#                 re.append(matrix[r][c2])
#             if r1 < r2 and c1 < c2:
#                 for c in range(c2-1, c1-1, -1):
#                     re.append(matrix[r2][c])
#                 for r in range(r2-1, r1, -1):
#                     re.append(matrix[r][c1])
#             r1 += 1
#             r2 -= 1
#             c1 += 1
#             c2 -= 1

#         return re
