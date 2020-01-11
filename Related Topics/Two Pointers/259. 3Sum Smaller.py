class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # O(n^2) since two sum smaller takes only O(n)
        nums.sort()
        count = 0
        
        def twoSumSmaller(nums, left, target):
            right = len(nums) - 1
            count = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
        
        for i in range(len(nums) - 2):
            count += twoSumSmaller(nums, i + 1, target - nums[i])
            
        return count
        