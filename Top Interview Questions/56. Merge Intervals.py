# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        re = [intervals[0]]
        intervals.pop(0)
        for i in intervals:
            j = re.pop()
            if j.end >= i.end:
                re.append(j)
                continue
            elif j.end >= i.start:
                re.append(Interval(j.start, i.end))
            else:
                re.append(j)
                re.append(i)
        return re