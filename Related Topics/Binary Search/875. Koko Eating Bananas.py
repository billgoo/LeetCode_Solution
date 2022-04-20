# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            hours = self.f(piles, mid)  # 单调递减函数
            if hours <= h:
                right = mid
            elif hours > h:
                left = mid + 1
        return left

    def f(self, piles: List[int], k: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours
