"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        - basically the trick is to sort the meetings by start time
        - then check if meeting 1's end is after meeting 2's start, if a conflict return false
        - else keep moving till the end, return true
        - complexity
            - time = O(nlogn)
            - space - O(1)
        """

        #sort
        intervals = sorted(intervals, key=lambda x: x.start)
        #check if overlapping
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
            else:
                continue

        #return true if not
        return True