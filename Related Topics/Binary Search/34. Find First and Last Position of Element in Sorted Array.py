# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        
        # find left bound
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        lo = l
        
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        
        # find right bound
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        
        return [lo, l - 1]
            