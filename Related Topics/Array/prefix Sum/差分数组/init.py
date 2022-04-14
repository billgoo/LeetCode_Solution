class Difference(object):

    def __init__(self, nums: List[int]) -> None:
        assert len(nums) > 0
        self.diff = nums[:]
        self.n = len(nums)
        for i in range(1, self.n):
            self.diff[i] = nums[i] - nums[i-1]

    def increment_range(self, i: int, j: int, val: int) -> None:
        if 0 <= i < self.n:
            self.diff[i] += val
        if 0 <= j + 1 < self.n:
            self.diff[j + 1] -= val

    def get_result_nums(self) -> List[int]:
        nums = self.diff[:]
        for i in range(1, self.n):
            # nums[i] = self.diff[i] + nums[i - 1]
            nums[i] += nums[i - 1]
        return nums
