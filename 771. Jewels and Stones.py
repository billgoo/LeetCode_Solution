class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_num = 0
        for j in J:
            jewels_num = jewels_num + S.count(j)
        return jewels_num