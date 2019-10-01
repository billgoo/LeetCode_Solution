class Solution:
    # Bit Manipulation
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     re = []
    #     nums.sort()
    #     
    #     for i in range(1 << len(nums)): # 2^length
    #         item = []
    #         for j in range(len(nums)):
    #             if i & (1 << j):
    #                 # 0001
    #                 # 0010
    #                 # 0100
    #                 item.append(nums[j])
    #         re.append(item)
    #     return re
    
    # Iteration
    def subsets(self, nums: List[int]) -> List[List[int]]:
        re = [[]]
        nums.sort()
        
        for num in nums:
            re.extend([item+[num] for item in re])
            
        return re
        
        