class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        d = dict()
        re = []
        
        if m <= n:
            for i in nums1:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for i in nums2:
                if i in d and d[i]:
                    d[i] -= 1
                    re.append(i)
        else:
            for i in nums2:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for i in nums1:
                if i in d and d[i]:
                    d[i] -= 1
                    re.append(i)
        return re
        