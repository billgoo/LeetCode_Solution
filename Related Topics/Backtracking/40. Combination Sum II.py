# 40. Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.backtrack(candidates, 0, target, 0, [], [])

    def backtrack(self, candidates: List[int], start: int, target: int,
                  curr_sum: int, curr_path: List[int], res: List[List[int]]
                  ) -> List[List[int]]:
        if curr_sum == target:
            res.append(curr_path[:])
            # return res
        # elif curr_sum > target:
        #     return res
        elif curr_sum < target:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr_path.append(candidates[i])
                curr_sum += candidates[i]
                res = self.backtrack(
                    candidates, i + 1, target, curr_sum, curr_path, res)
                curr_path.pop()
                curr_sum -= candidates[i]
        return res
