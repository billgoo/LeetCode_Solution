import heapq


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        q = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(q)
        if (-q[0][0]) > (len(S) + 1) / 2:
            return ""
        result = []
        while len(q) > 1:
            n1, c1 = heapq.heappop(q)
            n2, c2 = heapq.heappop(q)            
            result.append(c1)
            result.append(c2)
            if n1 < -1:
                heapq.heappush(q, (n1 + 1, c1))
            if n2 < -1:
                heapq.heappush(q, (n2 + 1, c2))
        return ''.join(result) + (q[0][1] if q else '')
        