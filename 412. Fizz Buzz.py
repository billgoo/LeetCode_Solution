class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = [str(i) for i in range(1, n+1)]
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                result[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                result[i - 1] = "Fizz"
            elif i % 5 == 0:
                result[i - 1] = "Buzz"
            i += 1
        return result
        