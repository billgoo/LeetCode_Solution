class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.tree = [0 for _ in range(n * 2)]
        self.tree[n:2*n] = nums[:]
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            

    def update(self, i: int, val: int) -> None:
        i += self.n
        temp = self.tree[i]
        self.tree[i] = val
        while i > 0:
            self.tree[i//2] += (val - temp)
            i //= 2
            

    def sumRange(self, i: int, j: int) -> int:
        i += self.n
        j += self.n
        sums = 0
        
        while i <= j:
            if i % 2 == 1:
                # right child then go to next left child
                sums += self.tree[i]
                i += 1
            if j % 2 == 0:
                # if left child then go to previous right child
                sums += self.tree[j]
                j -= 1
            # go to parents
            i //= 2
            j //= 2
        return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)