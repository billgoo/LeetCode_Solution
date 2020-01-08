# Calculate the a ^ n % b where a, b and n are all 32bit non-negative integers.
# Example: for 2 ^ 31 % 3 = 2

# Solution:
# (a ^ n) % b = ((a ^ n/2) % b * (a ^ n/2) % b) % b

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b

        result = self.fastPower(a, b, n // 2)
        result = (result * result) % b

        if n % 2 == 1:
            result = (result * a) % b

        return result