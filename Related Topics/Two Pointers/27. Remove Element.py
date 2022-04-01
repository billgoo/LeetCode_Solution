# 27. Remove Element
# 1. 左右指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr, tail = 0, len(nums) - 1
        while curr <= tail:
            if nums[curr] == val:
                nums[curr], nums[tail] = nums[tail], nums[curr]
                tail -= 1
            else:
                curr += 1
        return curr
# 2. 快慢指针
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         fast = slow = 0
#         n = len(nums)
#         while fast < n:
#             if nums[fast] != val:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#             fast += 1
#         return slow