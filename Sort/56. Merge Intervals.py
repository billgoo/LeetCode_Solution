class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        p = 0
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                if intervals[i][1] >= intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
                intervals[i], intervals[p] = intervals[p], intervals[i]
                p += 1
                
        return intervals[p:]