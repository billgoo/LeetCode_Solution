class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                if (exist(board, i, j, word, 0)) return true;
            }
        }
        return false;
    }
    
    public boolean exist(char[][] board, int x, int y, String word, int l) {
        if (l == word.length()) return true;
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length) return false;
        if (board[x][y] != word.charAt(l)) return false;
        
        board[x][y] = ' ';
        boolean re = exist(board, x - 1, y, word, l + 1)
            || exist(board, x + 1, y, word, l + 1)
            || exist(board, x, y - 1, word, l + 1)
            || exist(board, x, y + 1, word, l + 1);
        
        board[x][y] = word.charAt(l);
        return re;
    }
}