class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                m = max((j - i) * height[i], m)
                i += 1
            elif height[i] > height[j]:
                m = max((j - i) * height[j], m)
                j -= 1
            else:
                m = max((j - i) * height[i], m)
                if i + 1 < j:
                    m = max((j - i - 1) * min(height[i+1], height[j]), m)
                elif i < j - 1:
                    m = max((j - i - 1) * min(height[i], height[j-1]), m)
                i += 1
                j -= 1
        return m