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

