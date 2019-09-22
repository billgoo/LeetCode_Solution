class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # one pass for swap elem to the right position
        for i in range(n):
            while nums[i] > 0 and nums[i] < n and \
                nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        # check if i = nums[i]
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
            
        return n+1
        