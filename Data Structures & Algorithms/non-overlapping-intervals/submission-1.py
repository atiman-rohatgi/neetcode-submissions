class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        - sort the intervals, 
        - when two intervals overlap, greedy aproach is keeping the one with the smaller end as it allows more intervals later.
        - append res and keep the interval with the smaller end
        - complexity
            - time = O(nlogn)
            - space = O(1)
        """

        #sort
        intervals.sort(key = lambda x:x[0])

        #set things up
        res = 0 #intervals to be removed
        prev_end = intervals[0][1]

        #check for overlap
        for start, end in intervals[1:]:
            if start >= prev_end: #no overlap
                prev_end = end
            else: #overlap
                res += 1
                prev_end = min(prev_end, end)
        
        return res