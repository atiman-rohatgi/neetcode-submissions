class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        - two pre sorted lists with disjoint in their own context
        - interval is start(max of a,b) and end(min of a,b)
        - if the interval's start <= end, append
            - else dont
        - we use two pointers and move the one whose end is less
            - this works because the sets are disjoint, if Ea<Eb, then Ea would never intersect with elements after Eb.
        - edge: if either list empty, return empty
        - complexity
            - time = O(n)
            - space = O(n)
        """

        #edge
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        #set two pointers
        i, j = 0, 0
        output = []

        #main loop
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            #appending
            if start <= end:
                output.append([start, end])

            #move the pointer
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1 

        return output


