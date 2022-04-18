# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 沿对角线(i, i)反转
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 反转每行
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # matrix[:] = map(list, zip(*matrix[::-1]))

#         '''
#         Most Direct - 52 ms

#         A 100% in-place solution. It even reads and writes each matrix element
#         only once and doesn't even use an extra temporary variable to hold them.
#         It walks over the "top-left quadrant" of the matrix and directly rotates
#         each element with the three corresponding elements in the other three
#         quadrants. Note that I'm moving the four elements in parallel and that
#         [~i] is way nicer than [n-1-i].

#         class Solution:
#             def rotate(self, A):
#                 n = len(A)
#                 for i in range(n/2):
#                     for j in range(n-n/2):
#                         A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
#                                  A[~j][i], A[~i][~j], A[j][~i], A[i][j]
#         '''

#         n = len(matrix)
#         # reverse
#         for i in range(n//2):
#             matrix[i], matrix[~i] = matrix[~i], matrix[i]
#         # transpose
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
