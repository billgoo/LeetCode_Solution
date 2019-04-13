class Solution:
    def isHappy(self, n: int) -> bool:
        temp = sum(int(i) ** 2 for i in str(n))
        s = {temp}
        while temp != 1:
            temp = sum(int(i) ** 2 for i in str(temp))
            if temp in s:
                return False
            s.add(temp)
        return True