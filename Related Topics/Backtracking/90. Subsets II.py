# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.track = []
        self.res = []
        nums.sort()
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int) -> None:
        self.res.append(self.track[:])
        for i in range(start, len(nums)):
            # 遍历树剪枝
            if i - start > 0 and nums[i] == nums[i - 1]:
                continue

            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()
        return
