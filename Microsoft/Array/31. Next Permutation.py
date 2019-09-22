class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n-1, 0, -1):
            # get index i-1
            if nums[i] > nums[i-1]:
                for j in range(i, n):
                    # get index j-1
                    if nums[i-1] >= nums[j]:
                        nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
                        break
                else:
                    nums[i-1], nums[n-1] = nums[n-1], nums[i-1]
                    print(1,nums,i)
                
                # reverse the descending part
                for j in range(i, (n+i)//2):
                    nums[j], nums[n+i-1-j] = nums[n+i-1-j], nums[j]
                break
        else:
            # is the max permutation
            for i in range(n//2):
                nums[i], nums[~i] = nums[~i], nums[i]