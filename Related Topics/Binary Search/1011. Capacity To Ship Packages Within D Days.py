# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) == 0:
            return 0
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            need_days = self.f(weights, mid)
            if need_days <= days:
                right = mid
            else:
                left = mid + 1
        return left

    def f(self, weights: List[int], capacity: int) -> int:
        need_days = 0
        curr_cap = 0
        i, n = 0, len(weights)
        while i < n:
            while i < n and curr_cap + weights[i] <= capacity:
                curr_cap += weights[i]
                i += 1
            need_days += 1
            curr_cap = 0
        return need_days
