class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0, 1]
        pre = ' '
        
        if s <= ' ' or len(s) < 1:
            return 0
        
        for d in s:
            dp = [dp[1], dp[1]*int(d>'0')+dp[0]*int(9<int(pre+d)<27)]
            pre = d
            
        return dp[1]