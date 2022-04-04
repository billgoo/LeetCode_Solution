# 78. Subsets
class Solution:
    # Backtracking
    class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], level: int) -> None:
        self.res.append(self.path[:])

        for i in range(level, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i + 1)
            self.path.pop()
        return

    # Bit Manipulation
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     re = []
    #     nums.sort()

    #     for i in range(1 << len(nums)): # 2^length
    #         item = []
    #         for j in range(len(nums)):
    #             if i & (1 << j):
    #                 # 0001
    #                 # 0010
    #                 # 0100
    #                 item.append(nums[j])
    #         re.append(item)
    #     return re

    # Iteration
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     re = [[]]
    #     nums.sort()

    #     for num in nums:
    #         re.extend([item+[num] for item in re])

    #     return re