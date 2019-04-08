class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def push(self, x: int) -> None:
        self.l.append(x)
        

    def pop(self) -> int:
        return self.l.pop()
        

    def top(self) -> int:
        if len(self.l) > 0:
            return self.l[-1]
        else:
            return False
        

    def peekMax(self) -> int:
        if len(self.l) > 0:
            return max(self.l)
        else:
            return False
        

    def popMax(self) -> int:
        if len(self.l) > 0:
            i = 0
            for j in range(len(self.l)):
                if self.l[j] >= self.l[i]:
                    i = j
            return self.l.pop(i)
        else:
            return False


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()