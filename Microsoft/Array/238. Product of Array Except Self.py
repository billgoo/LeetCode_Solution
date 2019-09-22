class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        re = [1 for i in range(n)]
        
        # from left
        for i in range(1, n):
            re[i] *= re[i-1] * nums[i-1]
        
        # from right
        R = 1
        for i in range(n-1, -1, -1):
            re[i] *= R
            R *= nums[i]
        
        return re
        