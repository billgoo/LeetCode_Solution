class Solution {
    public int titleToNumber(String s) {
        int ini = 'A', re = 0;
        int l = s.length();
        for (int i = 1; i <= l; i++) {
            int cur = s.charAt(l - i);
            re += Math.pow(26, i - 1) * (cur - ini + 1);
        }
        return re;
    }
}