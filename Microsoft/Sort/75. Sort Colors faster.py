class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if p2 == i:
                    nums[p1], nums[i] = nums[i], nums[p1]
                else:
                    nums[p2], nums[p1], nums[i] = nums[p1], nums[i], nums[p2]
                p1 += 1; p2 += 1
            elif nums[i] == 1:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 += 1
            