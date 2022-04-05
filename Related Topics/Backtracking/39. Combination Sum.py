# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.backtrack(candidates, target, 0, [], 0, [])

    def backtrack(self, candidates: List[int], target: int, start: int,
                  path: List[int], pathSum: int, res: List[List[int]]) -> List[List[int]]:
        if pathSum == target:
            res.append(path[:])
            return res
        elif pathSum < target:
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                pathSum += candidates[i]
                res = self.backtrack(candidates, target, i, path, pathSum, res)
                path.pop()
                pathSum -= candidates[i]
        return res
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         re = []

#         def backtracking(re, temp_list, nums, remain, s):
#             if remain < 0:
#                 return
#             elif remain == 0:
#                 re.append(temp_list[:])
#             else:
#                 for i in range(s, len(nums)):
#                     temp_list.append(nums[i])
#                     backtracking(re, temp_list, nums, remain-nums[i], i)
#                     # back track
#                     temp_list.pop()

#         backtracking(re, [], candidates, target, 0)
#         return re
