class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        - the list is already sorted
        - we'd have three parts
            - if the end of intervals < new start, append those.
            - if there is overlapping then merge the overlap
            - if the start of intervals > new end, they will be also appeneded.
        - for the overlaps, the start would be the min of the two, while end will be the max of the two
        - complexity
            - time = O(n)
            - space = O(n)
        """

        #set things up
        res = []
        i = 0
        n = len(intervals)

        #part1
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        #part2
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        #part3
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

        