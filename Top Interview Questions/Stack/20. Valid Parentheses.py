class Solution:
    def isValid(self, s: 'str') -> 'bool':
        """
        # old version
        if len(s) == 0:
            return True
        if s[0] == ')' or s[0] ==']' or s[0] == '}':
            return False
        stack = []
        for i in s:
            if i == '(' or i =='[' or i == '{':
                stack.append(i)
            elif i == ')':
                if not stack or (stack.pop() != '('):
                    return False
            elif i == ']':
                if not stack or (stack.pop() != '['):
                    return False
            elif i == '}':
                if not stack or (stack.pop() != '{'):
                    return False
        if not stack:
            return True
        else:
            return False
        """

        # new and simplier version
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in mapping:
                if not stack or mapping[c] != stack.pop():
                    # have only right parenthese
                    return False
            else:
                stack.append(c)
                
        return not stack
        