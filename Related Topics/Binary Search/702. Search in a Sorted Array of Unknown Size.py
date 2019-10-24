class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # search boundaries
        right = 1
        while reader.get(right-1) < target:
            right <<= 1
        left = right >> 1
        
        # bi-search
        while left <= right:
            m = left + ((right - left) >> 1)
            num = reader.get(m)
            
            if num == target:
                return m
            elif num > target:
                right = m - 1
            else:
                left =  m + 1
                
        return -1