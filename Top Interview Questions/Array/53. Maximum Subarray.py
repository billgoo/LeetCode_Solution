class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        if len(nums) == 1:
            return nums[0]
        
        m = len(nums) // 2
        s = 0
        left_s = float('-inf')
        for i in range(m, -1, -1):
            s += nums[i]
            left_s = max(left_s, s)
            
        s = 0
        right_s = float('-inf')
        for i in range(m+1, len(nums)):
            s += nums[i]
            right_s = max(right_s, s)
            
        re = max(left_s, right_s, left_s + right_s)
        
        return max(self.maxSubArray(nums[:m]),
                    self.maxSubArray(nums[m+1:]),
                    re)
        