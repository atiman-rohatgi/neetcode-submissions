class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        - sort the intervals based on their starting
        - iterate and check if the the next intervals start <= end
        - if yes then use the min max rule to extedn the intervals
        - if no then append the current interval and move on
        - complexity
            - time = O(nlogn)
            - space = O(n)
        """
        
        #sort intervals
        intervals.sort(key = lambda x: x[0])

        #create an output array and other things
        i = 0
        n = len(intervals)
        output = []

        #iterate and append if needed
        while i < n:
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            while (i+1) < n and intervals[i+1][0] <= curr_end:
                curr_end = max(curr_end, intervals[i+1][1])
                i += 1
            
            output.append([curr_start, curr_end])
            i += 1
            
        #return
        return output
