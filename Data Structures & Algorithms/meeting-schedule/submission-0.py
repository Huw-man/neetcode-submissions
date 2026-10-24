"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        s_intervals = sorted(intervals, key=lambda i: i.start)
        for i, itv in enumerate(s_intervals):
            if i == 0:
                continue
            elif s_intervals[i-1].end > itv.start:
                return False
        return True
