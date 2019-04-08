class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        n = len(b)
        m = len(a)
        temp = 0
        re = ""
        while n > 0:
            if a[m - 1] == '1' and b[n - 1] == '1':
                if temp == 1:
                    re = "1" + re
                else:
                    re = "0" + re
                temp = 1
            else:
                c = int(a[m - 1]) + int(b[n - 1]) + temp
                if c > 1:
                    re = "0" + re
                    temp = 1
                else:
                    re = str(c) + re
                    temp = 0
            n -= 1
            m -= 1
            
        while m > 0:
            if int(a[m - 1]) + temp > 1:
                re = "0" + re
                temp = 1
            else:
                re = str(int(a[m - 1]) + temp) + re
                temp = 0
            m -= 1
        
        if temp == 1:
            re = "1" + re
        
        return re