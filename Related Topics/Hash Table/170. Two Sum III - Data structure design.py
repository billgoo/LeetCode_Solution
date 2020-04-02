class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_count = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.num_count:
            self.num_count[number] += 1
        else:
            self.num_count[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.num_count:
            if value - n in self.num_count:
                if value - n != n:
                    return True
                if self.num_count[n] > 1:
                    return True
            
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)