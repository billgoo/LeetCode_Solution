import heapq


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        q = [(-tasks.count(x), x) for x in set(tasks)]
        heapq.heapify(q)
        n0, c0 = heapq.heappop(q)
        num_idle = (-n0 - 1) * n        
        while len(q) > 0:
            n1, c1 = heapq.heappop(q)
            if n1 == n0:
                num_idle += (n1 + 1)
            else:
                num_idle += n1
            if num_idle < 0:
                return len(tasks)
        return len(tasks) + num_idle