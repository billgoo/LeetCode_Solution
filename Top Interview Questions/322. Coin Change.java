// bottom-up
class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = Integer.MAX_VALUE - amount;
        
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;
        //System.out.println(dp[amount]);
        
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
            }
        }
        return dp[amount] < max ? dp[amount] : -1;
    }
}

// top-down: important dp example
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount <= 0) return 0;
        return coinChange(coins, amount, new int[amount]);
    }
    
    public int coinChange(int[] coins, int amount, int[] counter) {
        if (amount < 0) return -1;
        else if (amount == 0) return 0;
        if (counter[amount - 1] != 0) return counter[amount - 1];
        
        int min = Integer.MAX_VALUE;
        
        for (int coin : coins) {
            int temp = coinChange(coins, amount - coin, counter);
            if (temp >= 0 & temp < min) min = temp;
        }
        counter[amount - 1] = (min < Integer.MAX_VALUE ? min + 1 : -1);
        return counter[amount - 1];
    }
}