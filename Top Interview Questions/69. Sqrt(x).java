class Solution {
    public int mySqrt(int x) {
        long xi = x / 2 + 1;
        
        while (xi * xi > x) {
            xi = (xi + x / xi) / 2;
        }
        
        return (int) xi;
    }
}