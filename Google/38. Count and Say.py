class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n == 0:
            return ""
        for i in range(n - 1):
            temp = []
            for j in range(len(s)):
                if not temp:
                    temp.append([1, s[j]])
                else:
                    if s[j] == temp[-1][1]:
                        temp[-1][0] += 1
                    else:
                        temp.append([1, s[j]])
            s = ""
            for j in temp:
                s += str(j[0]) + j[1]
            print(i + 1, s)
        return s