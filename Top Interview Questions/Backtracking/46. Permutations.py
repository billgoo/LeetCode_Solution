#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
# 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums)
        return self.res
        
    def backtrack(self, path: List[int], nums: List[int]) -> None:
        if len(nums) == 0:
            self.res.append(path[:])
            return
        for i, x in enumerate(nums):
            path.append(x)
            self.backtrack(path[:], nums[:i] + nums[i+1:])
            path.pop()
        return
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.res = []
#         track = []

#         def backtrack(nums, track):
#             n = len(nums)
#             if len(track) == n:
#                 self.res.append(track[:])
#                 return

#             for num in nums:
#                 if not num in track:
#                     track.append(num)
#                     backtrack(nums, track)
#                     track.pop()
#         backtrack(nums, track)
#         return self.res
# @lc code=end
# 2
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