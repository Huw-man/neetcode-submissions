"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s, e = 0, 0
        meetings = 0
        max_meetings = 0
        while s < len(intervals) and e < len(intervals):
            if starts[s] < ends[e]:
                meetings += 1
                s += 1
            elif ends[e] <= starts[s]:
                meetings -=1
                e += 1
            max_meetings = max(max_meetings, meetings)
        
        return max_meetings
            
        