class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n1 in nums2:
            if n1 in nums1:
                result.append(n1)
                nums1.remove(n1)
        return result
