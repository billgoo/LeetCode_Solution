class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        re = []
        
        def NSum(nums, target, N, result, results):
            if len(nums) < N or N < 2: return
            
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        results.append(result+[nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(0, len(nums)-N+1):
                    if target < nums[i]*N or target > nums[-1]*N:
                        break
                    if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                        NSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
            return results
        
        re = NSum(nums, target, 4, [], [])
        return re