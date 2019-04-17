class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            nums[2] = max(nums[1], nums[0] + nums[2])
            
            for i in range(3, n):
                nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

            return max(nums[n - 1], nums[n - 2])
            