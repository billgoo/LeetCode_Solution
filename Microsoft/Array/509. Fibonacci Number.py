# 509.Fibonacci Number
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 2 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(3, n + 1):
            s = prev + curr
            prev = curr
            curr = s
        return curr
        
"""
matrix solution
[ Fn     = [ 1 1   * [ Fn-1
  Fn-1 ]     1 0 ] *   Fn-2 ]
"""

