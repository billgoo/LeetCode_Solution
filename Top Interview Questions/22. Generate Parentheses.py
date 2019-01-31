class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if not n:
            return []
        
        result = ["("]
        counter = [[n - 1, n]]
        for i in range(2 * n):
            if len(result[0]) == 2 * n:
                return result
            l = len(result)
            for k in range(l):
                temp = result.pop(0)
                temp_c = counter.pop(0)
                if temp_c[0]:
                    result.append(temp+"(")
                    counter.append([temp_c[0]-1, temp_c[1]])
                if temp_c[1] - temp_c[0] >= 1:
                    result.append(temp+")")
                    counter.append([temp_c[0], temp_c[1]-1])
        return result