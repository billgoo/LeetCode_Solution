import random

class Solution:

    def __init__(self, w: 'List[int]'):
        self.w = w

    def pickIndex(self) -> 'int':
        num = random.uniform(0, sum(self.w))
        for i in range(len(self.w)):
            num -= self.w[i]
            if num < 0:
                return i
            elif num == 0:
                return random.choice([i, i+1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()