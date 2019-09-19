class Solution:
    def fib(self, N: int) -> int:
        F = [0, 1, 1]
        for i in range(3, N+1):
            F[i%3] = F[(i-2)%3] + F[(i-1)%3]
            
        return F[N%3]
        
"""
matrix solution
[ Fn     = [ 1 1   * [ Fn-1
  Fn-1 ]     1 0 ] *   Fn-2 ]
"""

