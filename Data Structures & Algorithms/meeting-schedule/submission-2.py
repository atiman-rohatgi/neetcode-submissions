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
        intervals.sort(key=lambda x: x.start)
        #check if overlapping
        prev_end = -1
        for interval in intervals:
            if interval.start < prev_end:
                return False
            prev_end = interval.end

        #return true if not
        return True