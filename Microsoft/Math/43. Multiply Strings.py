class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        product = [0 for _ in range(m+n)]
        
        for i in range(m):
            for j in range(n):
                product[i+j] += int(num1[m-1-i]) * int(num2[n-1-j])
                product[i+j+1] += product[i+j] // 10
                product[i+j] %= 10
        
        pt = 1
        for i in range(m+n-1, -1, -1):
            if product[i]:
                pt = i + 1
                break
        
        return ''.join(map(str, reversed(product[:pt])))