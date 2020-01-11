class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re = []
        
        # O(n^2)
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            f = i + 1; l = len(nums) - 1
            while f < l:
                s, e = nums[f], nums[l]
                if s + e + nums[i] == 0:
                    re.append([nums[i], s, e])
                    while f < l and nums[f] == nums[f+1]:
                        f += 1
                    while f < l and nums[l] == nums[l-1]:
                        l -= 1
                    f += 1; l -= 1
                elif s + e + nums[i] > 0:
                    l -= 1
                elif s + e + nums[i] < 0:
                    f += 1
                    
        return re