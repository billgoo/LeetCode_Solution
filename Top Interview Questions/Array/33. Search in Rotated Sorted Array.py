class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l, r = 0, len(nums) - 1
        pivot = 0
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                break
            else:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m
        pivot = l
        
        # bi search left
        l, r = 0, pivot - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        # bi search right
        l, r = pivot, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1
        