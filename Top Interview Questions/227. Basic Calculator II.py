class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        # s = s.replace(" ", "")
        st = []
        num, sign = 0, '+'
        
        for i in range(len(s)):
            c = s[i]
            # print(st,"b")
            if c.isdigit():
                num = int(c) + 10 * num
            
            if not (c.isdigit() or c.isspace()) or i == len(s) - 1:
                if sign == '+':
                    st.append(num)
                elif sign == '-':
                    st.append(-num)
                elif sign == '*':
                    st.append(st.pop()*num)
                elif sign == '/':
                    pre = st.pop()
                    if pre < 0:
                        st.append(-(abs(pre)//num))
                    else:
                        st.append(pre//num)
                num, sign = 0, c
            # print(st,"e")
        return sum(st)
        