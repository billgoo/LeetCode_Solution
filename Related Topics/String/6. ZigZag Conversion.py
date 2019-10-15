class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        explanation:
            visit the s by down->up->down->up
            when row = 0 or numRows-1, each down and up have only 1 num,
                which is index_in_s = row + 2 * (numRows - 1)
            when row = others, each have 1 down and 1 up, 2 nums,
                which is index_in_s = row + 2 * (numRows - 1)
                and then index_in_s = row + 2 * (numRows - 1 - i)
                then set index to (the index_in_s + 2 * (numRows - 1))
                to start the next down->up recurrence
        """
        l = len(s)
        if l <= numRows or numRows < 2:
            return s
        
        re = []
        for i in range(numRows):
            x = i
            while x < l:
                if x < l:
                    re.append(s[x])
                if 0 < i < numRows-1 and x+2*(numRows-1-i) < l:
                    re.append(s[x+2*(numRows-1-i)])
                x += 2*(numRows - 1)
        return ''.join(re)