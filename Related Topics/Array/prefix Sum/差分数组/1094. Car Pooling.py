# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        self.init_diff(1001)
        for [num, from_, to_] in trips:
            self.increment(from_, to_ - 1, num)
        res = self.get_res()
        for num in res:
            if num > capacity:
                return False
        return True

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
