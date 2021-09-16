# 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        return max(self.rob_range(nums, 0, n-2), self.rob_range(nums, 1, n-1))
        
    def rob_range(self, nums, start, end):
        dp_0 = dp_1 = dp_2 = 0
        for i in range(end, start - 1, -1):
            dp_0 = max(dp_1, dp_2 + nums[i])
            dp_2, dp_1 = dp_1, dp_0
        return dp_0