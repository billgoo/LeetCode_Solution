# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        res = [-1, -1]

        # find left
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == target:
            res[0] = left
        else:
            return res

        # find right
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # 这里判断右边界合法性，可以删除
        # 因为不存在右边界时 left = 0 => res[1] = left - 1 = -1
        # 且左边界合法，那必定存在右边界
        # if left - 1 >= 0 and nums[left - 1] == target:
        #     res[1] = left - 1

        return res