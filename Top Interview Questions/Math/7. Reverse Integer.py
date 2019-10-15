class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        MAX_VALUE, MIN_VALUE = 214748364, -214748364
        if x == 0:
            return x
        elif x > 0:
            while x != 0:
                digit = x % 10
                x = x // 10
                if result > MAX_VALUE or (result == MAX_VALUE and digit > 7):
                    return 0
                result = 10 * result + digit
        else:
            y = abs(x)
            while y != 0:
                digit = y % 10
                y = y // 10
                if result < MIN_VALUE or (result == MIN_VALUE and digit > 8):
                    return 0
                result = 10 * result - digit
        return result