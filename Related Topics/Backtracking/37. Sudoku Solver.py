class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)

    def backtrack(self, board: List[List[str]], i: int, j: int) -> bool:
        # 一行结束
        if j == 9:
            return self.backtrack(board, i + 1, 0)
        # 找到结果
        if i == 9:
            return True
        # 数字，跳过
        if board[i][j] != ".":
            return self.backtrack(board, i, j + 1)

        # 递归
        for k in range(9):
            number = str(k + 1)
            if not self.validSudoku(board, i, j, number):
                continue
            board[i][j] = number
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = "."
        return False

    def validSudoku(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        for i in range(9):
            if board[row][i] == char or board[i][col] == char:
                return False
            if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == char:
                return False
        return True
