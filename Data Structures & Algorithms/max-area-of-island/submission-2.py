class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        - this is a grid dfs problem, we do as deep to find max number
        - starting case would be any 1 we encounter, dfs 4-way, with a counter of how many 1s.
            - store the max count and all the connected 1's would be made 0's
        - after that, we will reset the count and dfs from a different starting point
        - complexity
         - time = O(m*n)
         - space = O(m*n)
        """

        #setting things up
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_area = 0

        #dfs
        def dfs(r, c):
            #base case
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == 0:
                return 0
            
            #mark
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area



        