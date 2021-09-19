# nSum
class Solution:
    def nSum(self, nums: List[int], n: int, target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, n, 0, len(nums), target)
        
    def nSumHelper(self, nums, n, start, length, target):
        res = []
        if n < 2 or n > length:
            return res
        if n == 2:
            return self.twoSum(nums, start, length - 1, target)
        else:
            i = start
            while i < length - n + 1:
                sub = self.nSumHelper(nums, n - 1, i + 1, length, target - nums[i])
                for s in sub:
                    s.append(nums[i])
                    res.append(s)
                while i < length - n + 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
            return res

    def twoSum(self, nums, l, r, target):
        res = []
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == target:
                res.append([nums[r], nums[l]])
                left = nums[l]
                while l < r and nums[l] == left:
                    l += 1
                right = nums[r]
                while l < r and nums[r] == right:
                    r -= 1
            elif sum_ > target:
                right = nums[r]
                while l < r and nums[r] == right:
                    r -= 1
            elif sum_ < target:
                left = nums[l]
                while l < r and nums[l] == left:
                    l += 1
        return res