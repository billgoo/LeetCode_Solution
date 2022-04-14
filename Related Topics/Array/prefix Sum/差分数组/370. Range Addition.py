# 370. Range Addition

from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        df = Difference([0 for _ in range(length)])
        for [i, j, value] in updates:
            df.increment_range(i, j, value)
        return df.get_result_nums()

    def test(self) -> None:
        length1 = 5
        updates1 = [[1,3,2],[2,4,3],[0,2,-2]]
        expected1 = [-2,0,3,5,3]
        res1 = self.getModifiedArray(length1, updates1)
        assert sum([res1[i] - expected1[i] for i in range(length1)]) == 0
        assert expected1 == res1
        print("pass case1")


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


s = Solution()
s.test()