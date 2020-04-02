class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        p1 = p2 = 0
        while p2 < n:
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                if p1 < p2:
                    p1 += 1
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 += 1
                    
        return p1 + 1