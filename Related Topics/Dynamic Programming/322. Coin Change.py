# 322. Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        
        # base case
        dp[0] = 0
        
        # status
        for i in range(amount + 1):
            # choices
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != amount + 1 else -1