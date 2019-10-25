class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        minPrice = float('inf')
        
        for i in prices:
            if i < minPrice:
                minPrice = i
                continue
            if m <= i - minPrice:
                m = i - minPrice
        
        return m