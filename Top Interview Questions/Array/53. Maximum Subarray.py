class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divide and conquer O_nlogn time and O_logn space
        if not nums:
            return float('-inf')
        if len(nums) == 1:
            return nums[0]
        
        m = len(nums) // 2

        # from m to the left, continue sum with m
        s = 0
        left_s = float('-inf')
        for i in range(m, -1, -1):
            s += nums[i]
            left_s = max(left_s, s)
        
        # from m to the right, continue sum with m
        s = 0
        right_s = float('-inf')
        for i in range(m+1, len(nums)):
            s += nums[i]
            right_s = max(right_s, s)
        
        # re is cross sum
        re = max(left_s, right_s, left_s + right_s)
        
        return max(self.maxSubArray(nums[:m]),
                    self.maxSubArray(nums[m+1:]),
                    re)
        
        """
        # greedy O_n time and O_1 space
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
        """

        """
        # greedy and dp O_n time and O_1 space
        n = len(nums)
        max_sum = nums[0]

        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
            
        return max_sum
        """

        """
        # greedy and dp from left and from right O_n time and O_n space
        n = len(nums)
        max_sum = nums[0]

        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
            
        return max_sum
        """