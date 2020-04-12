class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # bucket sort n+w time and w space
        bucket = [0 for _ in range(max(stones) + 1)]
        
        for w in stones:
            bucket[w] += 1
            
        curr = len(bucket) - 1
        y = 0
        while curr > 0:
            if bucket[curr] == 0:
                curr -= 1
            else:
                if y == 0:
                    bucket[curr] %= 2
                    if bucket[curr]:
                        y = curr
                    curr -= 1
                else:
                    bucket[curr] -= 1
                    if y - curr <= curr:
                        bucket[y - curr] += 1
                        y = 0
                    else:
                        y -= curr
        
        return y