class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        C0 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
             "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
              "Seventeen", "Eighteen", "Nineteen", "Twenty"]
        C1 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        E = ["Hundred", "Thousand", "Million", "Billion"]
        
        s_n = str(num)
        n = len(s_n)
        if n == 0:
            return ""
        elif n == 1:
            return C0[num]
        elif n == 2:
            if num <= 20:
                return C0[num]
            else:
                if int(s_n[1]) == 0:
                    return C1[int(s_n[0])]
                else:
                    return C1[int(s_n[0])] + " " + C0[int(s_n[1])]
        else:
            n_list = [int(x) for x in s_n]
            result = ""
            e = 0
            while len(n_list) != 0:
                d = []
                i = 0
                while len(n_list) != 0:
                    d.append(n_list.pop())
                    i += 1
                    if i == 3:
                        break
                        
                temp = ""
                if i == 1:
                    temp = C0[int(d[0])]
                elif i == 2:
                    if int(d[1])*10+int(d[0]) <= 20:
                        if int(d[1]+d[0]) != 0:
                            temp = C0[int(d[1])*10+int(d[0])]
                    else:
                        if int(d[0]) == 0:
                            temp = C1[int(d[1])]
                        else:
                            temp = C1[int(d[1])] + " " + C0[int(d[0])]
                else:
                    if int(d[2]) != 0:
                        temp = C0[int(d[2])] + " " + E[0]
                        if int(d[1])*10+int(d[0]) <= 20:
                            if int(d[1])*10+int(d[0]) != 0:
                                temp += " " + C0[int(d[1])*10+int(d[0])]
                        else:
                            if int(d[0]) == 0:
                                temp += " " + C1[int(d[1])]
                            else:
                                temp += " " + C1[int(d[1])] + " " + C0[int(d[0])]
                    else:
                        if int(d[1])*10+int(d[0]) <= 20:
                            if int(d[1])*10+int(d[0]) != 0:
                                temp += C0[int(d[1])*10+int(d[0])]
                        else:
                            if int(d[0]) == 0:
                                temp += C1[int(d[1])]
                            else:
                                temp += C1[int(d[1])] + " " + C0[int(d[0])]
                        
                
                if e >= 1:
                    if len(result) == 0:
                        if len(temp) != 0:
                            result = temp + " " + E[e]
                    else:
                        if len(temp) != 0:
                            result = temp + " " + E[e] + " " + result
                elif e == 0:
                    result = temp
                e += 1
            # end while
            return result
