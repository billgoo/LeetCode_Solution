class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        re = []

        def backtracking(re, temp_list, nums, remain, s):
            if remain < 0:
                return
            elif remain == 0:
                re.append(temp_list[:])
            else:
                for i in range(s, len(nums)):
                    temp_list.append(nums[i])
                    backtracking(re, temp_list, nums, remain-nums[i], i)
                    # back track
                    temp_list.pop()

        backtracking(re, [], candidates, target, 0)
        return re
