"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        - take 2 array, start and end, sort them
        - whenever conflict arises, room += 1, start += 1
        - if no conflict, then room -= 1 and end += 1
        - return the max
        - complexity
            - Time = O(nlogn)
            - Space = O(n)
        """
    
        #two arrays
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        #set things up
        rooms = 0
        max_rooms = 0
        s, e = 0, 0

        #the loop
        while s < len(start):
            #conflict
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else: #no conflict
                rooms -= 1
                e += 1
            
            max_rooms = max(max_rooms, rooms)

        #return max
        return max_rooms
