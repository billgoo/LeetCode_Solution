class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp, O(n) time one pass
        profit = 0
        n = len(prices)
        if n <= 1:
            return profit
        
        # to find one consequent valley and peak
        curr_min, curr_max = prices[0], prices[0]
        for i in range(1, n):
            if curr_max < prices[i]:
                # not reach peak
                curr_max = prices[i]
            else:
                # reach peak then go down, add the former peak - valley
                # and reset the entry valley
                profit += curr_max - curr_min
                curr_max = curr_min = prices[i]
                
        if curr_max > curr_min:
            profit += curr_max - curr_min
                
        return profit