class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ls, lt = len(S) - 1, len(T) - 1
        back_s = back_t = 0
        
        while ls >= 0 or lt >= 0:
            while ls >= 0 and (back_s > 0 or S[ls] == '#'):
                if S[ls] == '#':
                    back_s += 1
                else:
                    back_s -= 1
                ls -= 1
            while lt >= 0 and (back_t > 0 or T[lt] == '#'):
                if T[lt] == '#':
                    back_t += 1
                else:
                    back_t -= 1
                lt -= 1
            print(ls, lt)
            if ls >= 0 and lt >= 0:
                if S[ls] != T[lt]:
                    return False
                ls -= 1
                lt -= 1
            elif ls >= 0 or lt >= 0:
                return False
            
        return True