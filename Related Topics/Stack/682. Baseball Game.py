class Solution:
    def calPoints(self, ops: List[str]) -> int:
        self.score_stack = []
        # stimulation
        for char in ops:
            if char == "C":
                self.clear()
            elif char == "D":
                self.double()
            elif char == "+":
                self.add()
            else:
                self.score_stack.append(int(char))
        return sum(self.score_stack)

    def add(self) -> None:
        self.score_stack.append(sum(self.score_stack[-2:]))

    def double(self) -> None:
        self.score_stack.append(2 * self.score_stack[-1])

    def clear(self) -> None:
        self.score_stack.pop()
