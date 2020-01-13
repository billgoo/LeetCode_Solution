class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2)
        nums.sort()
        re = sum(nums[:3])
        
        for f in range(len(nums)):
            m, l = f + 1, len(nums) - 1
            while m < l:
                s = nums[f] + nums[m] + nums[l]
                if s > target:
                    l -= 1
                elif s < target:
                    m += 1
                else:
                    return target
                
                if abs(s-target) < abs(re-target):
                    re = s
                    
        return re