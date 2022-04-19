# 528. Random Pick with Weight
class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = [i for i in w]
        self.n = len(w)
        for i in range(1, self.n):
            self.pre_sum[i] += self.pre_sum[i - 1]

    def pickIndex(self) -> int:
        # num = random.randint(self.pre_sum[0], self.pre_sum[-1])
        num = random.uniform(0, self.pre_sum[-1])
        # bi-search
        left, right = 0, self.n
        while left < right:
            mid = left + (right - left) // 2
            if self.pre_sum[mid] == num:
                return mid
            elif self.pre_sum[mid] > num:
                right = mid
            else:
                left = mid + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()