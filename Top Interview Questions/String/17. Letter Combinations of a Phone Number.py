class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letter = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        def concat(digit, re):
            r = []
            for i in letter[int(digit)]:
                for j in re:
                    r.append(j+i)
            return r
        
        re = [""]
        for i in digits:
            re = concat(i, re)
            
        return re