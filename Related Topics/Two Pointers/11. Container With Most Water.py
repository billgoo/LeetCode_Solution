class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        i, j = 0, len(height) - 1
        
        while i < j:
            if height[i] < height[j]:
                m = max(m, (j-i)*height[i])
                i += 1
            elif height[i] > height[j]:
                m = max(m, (j-i)*height[j])
                j -= 1
            else:
                m = max(m, (j-i)*height[i])
                if i + 1 < j:
                    m = max(m, (j-i-1)*min(height[i+1], height[j]))
                if i < j - 1:
                    m = max(m, (j-i-1)*min(height[i], height[j-1]))
                i += 1; j -= 1
                
        return m        
                