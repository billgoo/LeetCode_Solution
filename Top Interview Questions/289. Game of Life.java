class Solution {
    public void gameOfLife(int[][] board) {
        /*
        states:
        0: 0 -> 0
        1: 1 -> 1
        2: 0 -> 1
        3: 1 -> 0
        */
        int[] nei = {-1, 0, 1};
        
        int r = board.length, c = board[0].length;
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int counter = 0;
                for (int n1 = 0; n1 < 3; n1++) {
                    for (int n2 = 0; n2 < 3; n2++) {
                        if (!(nei[n1] == 0 && nei[n2] == 0)) {
                            int row = i + nei[n1], col = j + nei[n2];
                            if (row >= 0 && row < r && col >= 0 && col < c) {
                                if (board[row][col] == 1 || board[row][col] == 3) {
                                    counter += 1;
                                }
                            }
                        }
                    }
                }
                // count neighbor ends
                
                if (board[i][j] == 1) {
                    if (counter < 2 || counter > 3)
                        board[i][j] = 3;
                } else {
                    if (counter == 3)
                        board[i][j] = 2;
                }
            }
        }
        // update ends
        
        // recover 2 and 3 to 1 and 0
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 2) {
                    board[i][j] = 1;
                }
                else if (board[i][j] == 3) {
                    board[i][j] = 0;
                }
            }
        }
    }
}