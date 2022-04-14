# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        self.init_diff(n)
        for [i, j, val] in bookings:
            self.increment(i - 1, j - 1, val)
        return self.get_res()

    def init_diff(self, length: int) -> None:
        self.diff = [0 for _ in range(length)]
        self.length = length

    def increment(self, i: int, j: int, val: int) -> None:
        if 0 <= i < self.length:
            self.diff[i] += val
        if 0 <= j + 1 < self.length:
            self.diff[j + 1] -= val

    def get_res(self) -> None:
        res = self.diff[:]
        for i in range(1, self.length):
            res[i] += res[i - 1]
        return res
