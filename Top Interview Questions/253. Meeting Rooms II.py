# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        
        h = []
        heapq.heappush(h, intervals[0].end)
        intervals.pop(0)
        
        for i in intervals:
            if h[0] <= i.start:
                heapq.heappop(h)
            
            heapq.heappush(h, i.end)
            
        return len(h)