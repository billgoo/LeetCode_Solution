class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1
        
        result = set()
        return self.dfs(s, 0, 0, 0, left, right, "", result)
        
        
        
    def dfs(self, s, index, left, right, left_r, right_r, temp, result):
        if index == len(s):
            if left_r == 0 and right_r == 0:
                result.add(temp)
        else:
            if s[index] == "(":
                result = set(self.dfs(s, index+1, left+1, right, left_r, right_r, temp+s[index], result))
                if left_r > 0:
                    result = set(self.dfs(s, index+1, left, right, left_r-1, right_r, temp, result))
            elif s[index] == ")":
                if right < left:
                    result = set(self.dfs(s, index+1, left, right+1, left_r, right_r, temp+s[index], result))
                if right_r > 0:
                    result = self.dfs(s, index+1, left, right, left_r, right_r-1, temp, result)
            else:
                result = set(self.dfs(s, index+1, left, right, left_r, right_r, temp+s[index], result))
        return list(result)
            