class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        comple = 1
        while temp:
            temp >>= 1
            comple <<= 1
            
        comple -= 1
        
        return num ^ comple