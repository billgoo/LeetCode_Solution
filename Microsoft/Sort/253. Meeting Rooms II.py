class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s = [i[0] for i in intervals]
        e = [i[1] for i in intervals]
        s.sort(); e.sort()
        
        i, j = 0, 0
        rooms = 0
        while i < len(s):
            rooms += 1
            if s[i] >= e[j]:
                rooms -= 1
                j += 1
            i += 1
        
        return len(e) - j