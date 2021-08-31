#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (49.25%)
# Likes:    4126
# Dislikes: 133
# Total Accepted:    208.8K
# Total Submissions: 423.2K
# Testcase Example:  '[1,2,3,0,2]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
# 
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Example 2:
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
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        dp_i_1_0 = 0
        for i in range(1, n):
            curr_0 = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_1_0 - prices[i])
            dp_i_1_0 = curr_0
        return dp_i_0
# @lc code=end

