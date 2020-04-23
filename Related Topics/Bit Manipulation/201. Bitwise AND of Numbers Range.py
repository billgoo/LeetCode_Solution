class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # bits shift
        """
        e = 0
        while m != n:
            m >>= 1
            n >>= 1
            e += 1
            
        return m << e
        """
        # Brian Kernighan's Algorithm
        # n & (n - 1) will remove the right most bits: 1100 & 1011 = 1000
        while m < n:
            n &= (n - 1)
            
        return m & n