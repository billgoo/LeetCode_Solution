"""
原题
在一个排序数组中找一个数，返回该数出现的最后一个位置，如果不存在，返回-1

给出数组 [1, 2, 2, 4, 5, 5]

对于 target = 2, 返回 2.
对于 target = 5, 返回 5.
对于 target = 6, 返回 -1.
解题思路
二分法，对于找最后一个位置的要求：只有target大于A[end]才会end = mid
"""

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A:
            return -1
    
    l, r = 0, len(A) - 1
    while l + 1 < r:
        m = (l + r) // 2
        if A[m] == target:
            l = m
        elif A[m] > target:
            r = m - 1
        else:
            l = m + 1

    if A[r] == target:
        return r
    elif A[l] == target:
        return l

    return -1

