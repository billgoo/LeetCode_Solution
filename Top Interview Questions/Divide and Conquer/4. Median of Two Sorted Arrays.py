class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        if n == 0:
            if m % 2:
                return nums1[m//2] * 1.0
            else:
                return (nums1[m//2-1] + nums1[m//2]) / 2.0
        
        # i and j are lower and upper bound of recurr on the longer list
        i, j, half = (m + n + 1) // 2 - n, (m + n + 1) // 2, (m + n + 1) // 2
        while i <= j:
            # sum of elements before p1 and before p2 is half
            p1 = (i + j) // 2   # index of the whole median in longer list
            p2 = half - p1  # index of the whole median in shorter list
            if p2 < n and nums1[p1-1] > nums2[p2]:
                # p1 left p2 to right
                j = p1 - 1
            elif p1 < half and nums1[p1] < nums2[p2-1]:
                # p1 right p2 to left
                i = p1 + 1
            else:
                if p2 == 0:
                    left_max = nums1[p1-1]
                elif p1 == 0:
                    # m == n else it will not be used
                    left_max = nums2[p2-1]
                else:
                    left_max = max(nums1[p1-1], nums2[p2-1])
                    
                if (m + n) % 2:
                    return left_max
                
                if p2 == n:
                    right_min = nums1[p1]
                elif p1 == m:
                    right_min = nums2[p2]
                else:
                    right_min = min(nums1[p1], nums2[p2])
                
                return (right_min + left_max) / 2.0