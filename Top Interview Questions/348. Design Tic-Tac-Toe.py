class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        # self.grid = [[0 for i in range(n)] for j in range(n)]
        self.row = [0 for i in range(n)]
        self.col = [0 for i in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # self.grid[row][col] = player
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagonal += 1
            if row + col + 1 == self.n:
                self.anti_diagonal += 1
            result = self.n
        else:   # player == 2
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diagonal -= 1
            if row + col + 1 == self.n:
                self.anti_diagonal -= 1
            result = -self.n
        
        # calculate the winning condition
        if self.row[row] == result or self.col[col] == result \
            or self.diagonal == result or self.anti_diagonal == result:
            return player
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)