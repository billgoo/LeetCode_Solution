class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> re = new ArrayList<Integer>();
        
        if (matrix.length == 0) return re;
        
        int lr = 0, rr = matrix.length - 1;
        int lc = 0, rc = matrix[0].length - 1;
        
        while (lr <= rr && lc <= rc) {
            for (int i = lc; i <= rc; i++) {
                re.add(matrix[lr][i]);
            }
            
            for (int i = lr + 1; i <= rr; i++) {
                re.add(matrix[i][rc]);
            }
            
            if (lr < rr && lc < rc){
                for (int i = rc - 1; i >= lc; i--) {
                    re.add(matrix[rr][i]);
                }

                for (int i = rr - 1; i > lr; i--) {
                    re.add(matrix[i][lc]);
                }
            }
            lr++;
            rr--;
            lc++;
            rc--;
        }
        
        return re;
    }
}