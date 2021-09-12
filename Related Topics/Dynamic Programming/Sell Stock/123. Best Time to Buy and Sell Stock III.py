#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (41.14%)
# Likes:    4288
# Dislikes: 96
# Total Accepted:    315.6K
# Total Submissions: 766.1K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
# 
# 
# Example 3:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
# Example 4:
# 
# 
# Input: prices = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # solution for all k
        # # standard with dp table
        # n = len(prices)
        # k = 2
        # # init
        # dp = [[[0 for i in range(2)] for j in range(k + 1)] for _ in range(n + 1)]
        # for i in range(n):
        #     for k_ in range(k, -1, -1):
        #         dp[i][k_][1] = float('-inf')
        # # dp loop
        # for i in range(n):
        #     for k_ in range(k, 0, -1):
        #         dp[i + 1][k_][0] = max(dp[i][k_][0], dp[i][k_][1] + prices[i])
        #         dp[i + 1][k_][1] = max(dp[i][k_][1], dp[i][k_ - 1][0] - prices[i])

        # return dp[n][k][0]

        # special case for k = 2 with less space
        # T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
        # T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
        # T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        # T[i][1][1] = max(T[i-1][1][1], -prices[i])
        n = len(prices)
        # init
        dp_20, dp_21 = 0, float('-inf')
        dp_10, dp_11 = 0, float('-inf')

        # dp loop
        for i in range(n):
            dp_20 = max(dp_20, dp_21 + prices[i])
            dp_21 = max(dp_21, dp_10 - prices[i])
            dp_10 = max(dp_10, dp_11 + prices[i])
            dp_11 = max(dp_11, 0 - prices[i])

        return dp_20
# @lc code=end

