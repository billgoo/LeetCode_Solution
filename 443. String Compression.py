class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return n
        
        r = w = 0
        a = 0
        c = chars[0]
        t = 0
        while r < n:
            if r != n - 1:
                if chars[r] != c:
                    chars[w] = c
                    w += 1
                    t += 1
                    if r - a > 1:
                        num = str(r - a)
                        for i in num:
                            chars[w] = i
                            w += 1
                            t += 1
                    c = chars[r]
                    a = r
            else:
                chars[w] = c
                w += 1
                t += 1
                if chars[r] != c:
                    if r - a > 1:
                        num = str(r - a)
                        for i in num:
                            chars[w] = i
                            w += 1
                            t += 1
                    chars[w] = chars[r]
                    t += 1
                else:
                    num = str(r - a + 1)
                    for i in num:
                        chars[w] = i
                        w += 1
                        t += 1
            r += 1
        return t
