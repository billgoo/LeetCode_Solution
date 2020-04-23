class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells or len(cells) == 0 or N <= 0:
            return cells
        
        ans = cells[:]
        
        def helper():
            p = ans[0]
            if ans[0]:
                ans[0] = 0
                
            for i in range(1, 7):
                nextDay = (p ^ ans[i + 1])  ^ 1
                p, ans[i] = ans[i], nextDay
                
            if ans[-1]:
                ans[-1] = 0
                
        if ans[0] or ans[-1]:
            helper()
            N -= 1
            
        s = set([''.join([str(i) for i in ans[1:7]])])
        
        # find pattern
        hasCycle = False
        while N > 0 and len(s) < 65:
            helper()
            key = ''.join([str(i) for i in ans[1:7]])
            N -= 1
            if key in s:
                hasCycle = True
                break
            else:
                s.add(key)
                
        if hasCycle:
            N %= len(s)
        for i in range(N):
            helper()
            
        return ans