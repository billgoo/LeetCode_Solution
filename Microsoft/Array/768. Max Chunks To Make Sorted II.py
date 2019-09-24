class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, (0, 0)
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans
        