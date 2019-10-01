class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                # 深拷贝 nums[:] = nums.copy()
                re.append(nums.copy())
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        re = []
        backtrack(0)
        
        return re