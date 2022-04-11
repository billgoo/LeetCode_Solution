# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # old
        # nums.sort()
        # re = []

        # # O(n^2)
        # for i in range(len(nums) - 2):
        #     if nums[i] > 0:
        #         break
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     f = i + 1; l = len(nums) - 1
        #     while f < l:
        #         s, e = nums[f], nums[l]
        #         if s + e + nums[i] == 0:
        #             re.append([nums[i], s, e])
        #             while f < l and nums[f] == nums[f+1]:
        #                 f += 1
        #             while f < l and nums[l] == nums[l-1]:
        #                 l -= 1
        #             f += 1; l -= 1
        #         elif s + e + nums[i] > 0:
        #             l -= 1
        #         elif s + e + nums[i] < 0:
        #             f += 1

        # return re

        # new for respect to 2 sum
        res = []
        nums.sort()

        n = len(nums)
        i = 0
        while i < n - 1:
            temp = self.twoSum(nums, i + 1, n - 1, -nums[i])
            if temp:
                for t in temp:
                    res.append([nums[i], t[0], t[1]])
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def twoSum(self, nums, l, r, target):
        res = []
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == target:
                res.append([nums[l], nums[r]])
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
        return res if len(res) > 0 else None
