# 47. Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.track = []
        self.backtrack(nums, len(nums))
        return self.res

    def backtrack(self, nums: List[int], level: int) -> None:
        if len(self.track) == level:
            self.res.append(self.track[:])
            return

        for i in range(len(nums)):
            # 剪枝
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.track.append(nums[i])
            self.backtrack(nums[:i] + nums[i + 1:], level)
            self.track.pop()
        return
