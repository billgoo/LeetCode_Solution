class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        m, n = len(S), len(T)
        s, t = [], []
        for i in S:
            if i != "#":
                s.append(i)
            else:
                if len(s) > 0:
                    s.pop()
        
        for i in T:
            if i != "#":
                t.append(i)
            else:
                if len(t) > 0:
                    t.pop()
                    
        return s == t
    