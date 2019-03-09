class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            i = m - 1
            j = n - 1
            c = 1
            while i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[m+n-c], nums1[i] = nums1[i], 0
                    i -= 1
                else:
                    nums1[m+n-c] = nums2[j]
                    j -= 1
                c += 1
            while j >= 0:
                nums1[m+n-c] = nums2[j]
                j -= 1
                c += 1
                    
        