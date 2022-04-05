# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.track = []
        self.backtrack(range(1, 10), 0, k, n)
        return self.res

    def backtrack(self, nums: List[int], start: int, k: int, n: int) -> None:
        if len(self.track) > k or n < 0:
            return
        if len(self.track) == k and n == 0:
            self.res.append(self.track[:])

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums, i + 1, k, n - nums[i])
            self.track.pop()
        return
