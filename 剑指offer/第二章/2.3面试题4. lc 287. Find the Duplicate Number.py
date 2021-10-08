# 剑指 offer 第二章 2.3 数据结构 - 数组，面试题 4
# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            c = 0
            for n in nums:
                if l <= n <= mid:
                    c += 1
            if c > (mid - l + 1):
                r = mid
            else:
                l = mid + 1
        return l if l in nums else -1
