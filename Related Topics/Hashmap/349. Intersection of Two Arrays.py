class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        temp = {}
        for n1 in nums1:
            if n1 not in temp:
                temp[n1] = n1
        for n2 in nums2:
            if n2 in temp and n2 not in result:
                result.append(n2)

        return result
