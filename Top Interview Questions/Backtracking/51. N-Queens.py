#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (53.54%)
# Likes:    3935
# Dislikes: 122
# Total Accepted:    294.4K
# Total Submissions: 549.7K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        board = ["." * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.result

    def backtrack(self, board, row):
        n = len(board)
        if row == n:
            self.result.append(board[:])
            return

        for col in range(n):
            if self.isValid(board, row, col):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                self.backtrack(board, row + 1)
                board[row] = board[row][:col] + "." + board[row][col + 1:]

    def isValid(self, board, row, col):
        n = len(board)

        # 验证上方列
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # 验证左上
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False

        # 验证右上
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == "Q":
                return False

        return True
# @lc code=end


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.backtrack(["." * n for _ in range(n)], 0, [], [], [])
        return self.res

    def backtrack(self, board: List[str], row: int, col_set: List[int],
                  left_set: List[int], right_set: List[int]) -> None:
        if row == len(board):
            self.res.append(board[:])
        for c in range(len(board)):
            if not self.isValid(row, c, col_set, left_set, right_set):
                continue

            # add
            board[row] = board[row][:c] + "Q" + board[row][c + 1:]
            # col_set.append(c)
            # left_set.append(r - c)
            # right_set.append(r + c)

            # recursion
            self.backtrack(board[:], row + 1, col_set[:] + [c],
                           left_set[:] + [row - c], right_set[:] + [row + c])

            # remove
            board[row] = board[row][:c] + "." + board[row][c + 1:]
            # col_set.pop()
            # left_set.pop()
            # right_set.pop()

        return

    def isValid(self, row: int, col: int, col_set: Set[int], left_set: Set[int], right_set: Set[int]) -> bool:
        # 从上到下从左到右，row/col 都增大
        # 故仅需检查：列上部分、左上、右上
        # 列：c in col_set, len = n
        # 左上：r - c in left_set, len = n: r - c = (r - 1) - (c - 1)
        # 右上：r + c in right_set, len = n: r + c = (r - 1) + (c + 1)
        if col in col_set:
            return False
        if row - col in left_set:
            return False
        if row + col in right_set:
            return False
        return True
