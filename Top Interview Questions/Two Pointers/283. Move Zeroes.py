class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n > 1:
            p1 = p2 = 0
            
            while p1 < n and p2 < n:
                if nums[p2]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                p2 += 1
        