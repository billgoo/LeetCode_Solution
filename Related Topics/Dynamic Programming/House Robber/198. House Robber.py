# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 自底向上
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        # # inplace solution with full memo
        # else:
        #     nums[2] = max(nums[1], nums[0] + nums[2])

        #     for i in range(3, n):
        #         nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

        #     return max(nums[n - 1], nums[n - 2])

        # # general dp solution with full memo
        # dp = [-1 for _ in range(n)]
        # dp[0], dp[1] = max(0, nums[0]), max(nums[0:2])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        # return dp[n-1]

        # simplify solution with less memo
        dp_0, dp_1 = nums[0], max(nums[:2])
        dp_2 = 0
        for i in range(2, n):
            dp_2 = max(dp_0 + nums[i], dp_1)
            dp_0, dp_1 = dp_1, dp_2

        return dp_2

        # 自顶向下
        # dp_i = 0
        # dp_1 = dp_2 = 0
        # for i in range(n - 1, -1, -1):
        #     dp_i = max(dp_1, nums[i] + dp_2)
        #     dp_1, dp_2 = dp_i, dp_1
        # return dp_i
