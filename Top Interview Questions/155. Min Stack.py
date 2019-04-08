class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m = float('inf')
        self.stack = []

        
    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.m = x
        else:
            self.stack.append(x - self.m)
            self.m = min(self.m, x)

            
    def pop(self) -> None:
        if len(self.stack) > 0:
            p = self.stack.pop()
            self.m -= p if p < 0 else 0
        
        
    def top(self) -> int:
        t = self.stack[-1]
        return (t + self.m if t > 0 else self.m)
        

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()