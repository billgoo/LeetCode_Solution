# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = [set() for _ in range(9)], [set() for _ in range(9)]
        cube = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    if c in row[i]:
                        return False
                    else:
                        row[i].add(c)
                    if c in col[j]:
                        return False
                    else:
                        col[j].add(c)
                    if c in cube[i//3][j//3]:
                        return False
                    else:
                        cube[i//3][j//3].add(c)
        return True
