class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b, a = a, b
        re = ""
        ad = 0
        for i in range(-1, -len(a)-1, -1):
            tmp = int(a[i]) + int(b[i]) + ad
            re = str(tmp % 2) + re
            ad = tmp // 2
            
        for i in range(-len(a)-1, -len(b)-1, -1):
            tmp = int(b[i]) + ad
            re = str(tmp % 2) + re
            ad = tmp // 2
            
        if ad:
            re = "1" + re
            
        return re
            