class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pass
        """
        - the objective is to add a spaceat indexes from spaces
        - we can create a empty list and append till the given spaces index, then add space.
        - combine the elments in the end
        - Complexity
            - time = O(n)
            - space = O(n)
        """

        #set things up
        res = []
        prev = 0

        #main loop
        #for all the index inside
        for idx in spaces:
            res.append(s[prev:idx])
            res.append(" ")
            prev = idx
        
        #now the leftover string
        res.append(s[prev:])

        #returning the main joined
        return "".join(res)