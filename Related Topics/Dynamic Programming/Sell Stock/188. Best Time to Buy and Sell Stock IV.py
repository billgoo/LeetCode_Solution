#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (31.27%)
# Likes:    2912
# Dislikes: 148
# Total Accepted:    200.9K
# Total Submissions: 639.6K
# Testcase Example:  '2\n[2,4,1]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete at most k
# transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
#
#
# Example 2:
#
#
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
# = 3-0 = 3.
#
#
#
# Constraints:
#
#
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
#
#
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2:
            dp_0, dp_1 = 0, float('-inf')
            for p in prices:
                temp = dp_0
                dp_0 = max(dp_0, dp_1 + p)
                dp_1 = max(dp_1, temp - p)
            return dp_0
        else:
            dp_ik0 = [0 for _ in range(k + 1)]
            dp_ik1 = [float('-inf') for _ in range(k + 1)]
            for p in prices:
                for k_ in range(k, 0, -1):
                    dp_ik0[k_] = max(dp_ik0[k_], dp_ik1[k_] + p)
                    dp_ik1[k_] = max(dp_ik1[k_], dp_ik0[k_ - 1] - p)
            return dp_ik0[k]
# @lc code=end
