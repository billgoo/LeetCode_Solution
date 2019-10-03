class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        re = sign * int(str(abs(x))[::-1])
        return re if -2**31 < re < 2**31 else 0
    