# 77. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.track = []
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start: int, n: int, k: int) -> None:
        if len(self.track) == k:
            self.res.append(self.track[:])
            return

        for i in range(start, n + 1):
            self.track.append(i)
            self.backtrack(i + 1, n, k)
            self.track.pop()

        return
