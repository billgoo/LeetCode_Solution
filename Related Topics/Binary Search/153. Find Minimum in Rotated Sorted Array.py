class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # find pivot
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] <= nums[r]:
                break
            else:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m
        # pivot = l
        
        return min(nums[0], nums[l])
        