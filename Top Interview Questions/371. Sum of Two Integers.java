class Solution {
    public int getSum(int a, int b) {
        int re = b == 0 ? a : getSum(a ^ b, (a & b) << 1);
        return re;
    }
}