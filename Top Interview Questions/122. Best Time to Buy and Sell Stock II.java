class Solution {
    public int maxProfit(int[] prices) {
        int t = 0;
        for (int i = 1; i < prices.length; i++) {
            t += (prices[i] - prices[i - 1] > 0) ? prices[i] - prices[i - 1] : 0;
        }
        return t;
    }
}