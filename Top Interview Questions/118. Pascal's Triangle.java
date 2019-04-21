class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri = new ArrayList<List<Integer>>();
        
        if (numRows == 0) {
            return tri;
        }
        
        tri.add(new ArrayList<>());
        tri.get(0).add(1);
        
        for (int r = 1; r < numRows; r++) {
            List<Integer> row = new ArrayList<>();
            List<Integer> pre = tri.get(r - 1);
            
            row.add(1);
            
            for (int c = 1; c < r; c++) {
                row.add(pre.get(c - 1) + pre.get(c));
            }
            
            row.add(1);
            tri.add(row);
        }
        
        return tri;
    }
}