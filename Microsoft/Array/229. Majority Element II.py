class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        can1, can2 = 0, 1
        
        for n in nums:
            if can1 == n:
                c1 += 1
            elif can2 == n:
                c2 += 1
            elif c1 == 0:
                can1, c1 = n, 1
            elif c2 == 0:
                can2, c2 = n, 1
            else:
                c1 -= 1; c2 -= 1
        
        c1, c2 = 0, 0
        for n in nums:
            if can1 == n:
                c1 += 1
            elif can2 == n:
                c2 += 1
        
        return [n[0] for n in [[can1, c1], [can2, c2]]\
                if n[1]>len(nums)/3]
        