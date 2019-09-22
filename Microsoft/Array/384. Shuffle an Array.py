class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums  # get obj
        self.ori_nums = list(self.nums)  # get just value

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums[:] = self.ori_nums[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        for i in range(0, n):
            ri = random.randint(i,n-1)
            self.nums[i], self.nums[ri] = self.nums[ri], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()