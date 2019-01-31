class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        re = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = -nums[i]
            f =  i + 1
            l = len(nums) - 1
            
            while f < l:
                start, end = nums[f], nums[l]
                if s == start + end:
                    a = [-s, start, end]
                    re.append([nums[i], start, end])
                    while f < l and nums[f] == nums[f+1]:
                        f += 1
                    while f < l and nums[l] == nums[l-1]:
                        l -= 1
                    f += 1
                    l -= 1
                elif s < start + end:
                    l -= 1
                elif s > start + end:
                    f += 1
        return re