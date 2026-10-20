class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - basically the question ask if we drop water on cell would it reach both the oceans, if yes then it is part of the result
        - we will do grid dfs
            - we go oppsoiute from the edge cells and make sure to climb upwards and append them
        - dfs to find the pacific list, then atlantic list and return the intersection of the two
        - complexity
            - time = O(m*n)
            - space = O(m*n)
        """
        
        #setting things up
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        #dfs function
        def dfs(r, c, visited, prev_h):
            #exit
            if not (0 <= r < rows) or not (0<= c < cols) or (r,c) in visited or heights[r][c] < prev_h:
                return

            #store
            visited.add((r,c))

            #explore all
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, visited, heights[r][c])

        #dfs from edges
        #top
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
        #left
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
        #right
        for r in range(rows):
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        #bottom
        for c in range(cols):
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        #the overlapping cells
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res
