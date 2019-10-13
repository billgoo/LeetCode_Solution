class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        mapping = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in mapping:
                return [i, mapping.get(target - nums[i])]
            else:
                mapping[nums[i]] = i
        return None