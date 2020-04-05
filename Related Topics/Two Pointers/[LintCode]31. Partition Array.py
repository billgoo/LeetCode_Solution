class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
            
        bound = 0
        n = len(nums)
        for i in range(n):
            # TODO: write code...
            if nums[i] < k:
                nums[bound], nums[i] = nums[i], nums[bound]
                bound += 1
        
        return bound