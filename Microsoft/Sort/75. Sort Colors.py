class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        k = len(nums) - 1
        while k > j:
            if nums[k] == 2:
                k -= 1
            elif nums[k] == 1:
                nums[k], nums[j] = nums[j], 1
                j += 1
            elif nums[k] == 0:
                nums[k], nums[j] = nums[j], 1
                nums[i] = 0
                i += 1
                j += 1
        if k == j:
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]