class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        m = 0
        for i, num in enumerate(arr):
            m = max(m, num)
            if m == i:
                ans += 1
        return ans
        