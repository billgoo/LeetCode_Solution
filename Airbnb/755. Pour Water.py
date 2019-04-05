class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        l = len(heights)
        if sum(heights) + V >= l * 99:
            return [99] * l
        
        for w in range(V):
            is_pour = False
            i = K - 1
            m = heights[K]
            j = K
            
            while i >= 0 and not is_pour and heights[i] <= heights[i + 1]:
                if m > heights[i]:
                    m, j = heights[i], i
                i -= 1
            if j != K:
                heights[j] += 1
                is_pour = True
                
            i = K + 1
            m = heights[K]
            j = K
            while i < l and not is_pour and heights[i] <= heights[i - 1]:
                if m > heights[i]:
                    m, j = heights[i], i
                i += 1
            if j != K:
                heights[j] += 1
                is_pour = True
            
            if not is_pour:
                heights[j] += 1
                
        return heights