# 303. Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
