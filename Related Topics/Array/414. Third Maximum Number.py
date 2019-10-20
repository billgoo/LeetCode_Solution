class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = [float('-inf')] * 3
        
        for i in range(len(nums)):
            if not nums[i] in temp:
                if nums[i] > temp[0]:
                    temp = [nums[i], temp[0], temp[1]]
                elif nums[i] > temp[1]:
                    temp[1:] = [nums[i], temp[1]]
                elif nums[i] > temp[2]:
                    temp[2] = nums[i]
        
        return temp[2] if not float('-inf') in temp else max(nums)