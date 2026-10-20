class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - way to calculate the number of islands is how many islands can we sink
            - when we encounter 1, count += 1, then call dfs to sink.
            - if another 1 found, count increment.
        - branch in 4 directions, as long as within the boundaries and is a 1
        - make the one visited as 0, to simulate sinking
        - complexity
            - time = O(m*n)
            - space = O(m*n)
        """
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            #base case
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == "0":
                return 

            #mark / store
            grid[r][c] = "0" #sinking the island

            #recurse
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in direction:
                dfs(r+dr, c+dc)

        #return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count


        